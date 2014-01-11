import google
from mixpanel import Mixpanel

mp = Mixpanel('752f301471ad54cb0cc0c8ce77f200da')

keywords = ['no essay scholarships']
our_domain = 'http://scholarhippo.com'

for keyword in keywords:
    results = google.search(keyword, stop=50)
    rank = 1
    ranked = False
    for result in results:
        if our_domain in result:
            print 'Found {} at {}'.format(our_domain, rank)
            ranked = True
            break
        rank += 1
    if not ranked:
        rank = -1
    mp.track(0, 'serp rank', {
    'Search Engine': 'google',
    'rank': rank,
    'keyword': keyword
    })