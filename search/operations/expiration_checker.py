# check every non-expired scholarship to see if it still exists
import os
import socket
import requests
from requests.exceptions import *
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scholarhippo.settings")

from search.models import Scholarship

error_strings = ['<TITLE>404 Not Found</TITLE>',
                 '<title>The resource cannot be found.</title>',
                 '<title>404 Not Found</title>'
                ]


def isScholarshipInPage(html):
    #check for some strings in the page that would suggest this scholarship is expired
    is_scholarship_in_page = True
    for e in error_strings:
        # check first 500 bytes of file for the not found string.
        # this is because some files are megabyte-long pdfs
        if e in html[:500]:
            is_scholarship_in_page = False

    return is_scholarship_in_page


# makes a request to see if scholarship model exists
def does_scholarship_exist(scholarship):
    # hit the url and check for 404
    try:
        response = requests.get(scholarship.third_party_url, timeout=30,
                                headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) ' +
                                                       'AppleWebKit/537.36 (KHTML, like Gecko) ' +
                                                       'Chrome/27.0.1453.116 Safari/537.36'})
    except ConnectionError:
        print 'Connection error'
        return False
    except Timeout:
        print 'Read timeout'
        return False
    except socket.error:
        print 'Socket Error'
        return False

    if response.status_code != 200:
        print 'Got a ' + str(response.status_code)
        return False
    if response.headers['content-type'] == 'application/pdf':
        return True
    elif not isScholarshipInPage(response.text):
        print 'Got a 200 response, but scholarship was not in the page.'
        return False
    return True


def expire():
    # get all unexpired scholarships
    scholarships = Scholarship.objects.filter(status=0)

    # we will give the failures a second chance once we hit everything.
    retry_list = []
    i = 1
    for s in scholarships:
        print ' #### checking ' + s.title + ' ####'
        print str(i) + ' / ' + str(len(scholarships))
        i += 1
        if not does_scholarship_exist(s):
            retry_list.append(s)
        else:
            print 'Found it!'

    expired_count = 0
    # process the retries
    for s in retry_list:
        if not does_scholarship_exist(s):
            #mark as expired and save
            s.status = 1
            s.save()
            expired_count += 1

    print 'Expired ' + str(expired_count) + ' scholarships out of ' + str(len(scholarships))



