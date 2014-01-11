import re
from django.http import HttpResponsePermanentRedirect
from pyDes import *
import base64
secret_key = 'Fitzgeralds remarks abou'
crypt = triple_des(secret_key, mode=ECB, padmode=PAD_PKCS5)

def is_empty(str):
    if str is None:
        return True
    elif str == '':
        return True
    else:
        return False

def int_to_bytes(data):
    assert isinstance(data, int), 'input was not an int'
    byte_array = []
    for s in 24,16,8,0:
        byte_array.append(((data >> s) & 0xff))
    return byte_array

def bytes_to_int(data):
    assert len(data) == 4, 'must pass in a str/collection of 4 elements'
    return (
        (ord(data[0]) & 0xff) << 24 |
        (ord(data[1]) & 0xff) << 16 |
        (ord(data[2]) & 0xff) << 8 |
        (ord(data[3]) & 0xff)
        )
# decrypt scholarship key (outputs scholarship id)
def decrypt_sk(sk):

    assert isinstance(sk, basestring) and len(sk) == 16, (
        'scholarship key was not a valid string')
    encrypted_byte_array = []
    for i in re.findall('..', sk):
        encrypted_byte_array.append(chr(int(i,16)))
    bytes = ''.join(encrypted_byte_array)
    return str(bytes_to_int( crypt.decrypt(bytes) ))

#encrypt scholarship id (outputs scholarship key)
def encrypt_sid(sid):
    assert isinstance(sid, basestring), 'scholarship id was not a string'
    sid_chars = []
    for ch in int_to_bytes(int(sid)):
        sid_chars.append(chr(ch))
    sid_enc = crypt.encrypt(sid_chars)
    return ''.join("{:02x}".format(ord(c)) for c in sid_enc)

def test_encryption():
    x = str(1234567890)
    print x
    y = encrypt_sid(x)
    print y
    print decrypt_sk(y)

#test_encryption()
def parse_string_param(param, default):
    if param is None or param == '':
        return default
    else:
        return param

def parse_int_param(param, default):
    try:
        parsed = int(param)
    except TypeError:
        parsed = default
    except ValueError:
        parsed = default
    return parsed

def parse_boolean_param(param):
    parsed = param == 'true' or param == 'True' or param == '1'
    return parsed

states_name_to_codes = {
    'alabama': 'AL',
    'alaska': 'AK',
    'arkansas': 'AR',
    'arizona': 'AZ',
    'california': 'CA',
    'colorado': 'CO',
    'connecticut': 'CT',
    'district-of-columbia': 'DC',
    'delaware': 'DE',
    'florida': 'FL',
    'georgia': 'GA',
    'hawaii': 'HI',
    'iowa': 'IA',
    'idaho': 'ID',
    'illinois': 'IL',
    'indiana': 'IN',
    'kansas': 'KS',
    'kentucky': 'KY',
    'louisiana': 'LA',
    'massachusetts': 'MA',
    'maryland': 'MD',
    'maine': 'ME',
    'michigan': 'MI',
    'minnesota': 'MN',
    'missouri': 'MO',
    'mississippi': 'MS',
    'montana': 'MT',
    'north-carolina': 'NC',
    'north-dakota': 'ND',
    'nebraska': 'NE',
    'new-hampsire': 'NH',
    'new-jersey': 'NJ',
    'new-mexico': 'NM',
    'nevada': 'NV',
    'new-york': 'NY',
    'ohio': 'OH',
    'oklahoma': 'OK',
    'oregon': 'OR',
    'pennsylvania': 'PA',
    'puerto-rico': 'PR',
    'rhode-island': 'RI',
    'south-carolina': 'SC',
    'south-dakota': 'SD',
    'tennessee': 'TN',
    'texas': 'TX',
    'utah': 'UT',
    'virgina': 'VA',
    'vermont': 'VT',
    'washington': 'WA',
    'wisconsin': 'WI',
    'west-virgina': 'WV',
    'wyoming': 'WY'
}

states_codes_to_names = {
    'AL': 'Alabama',
    'AK': 'Alaska',
    'AR': 'Arkansas',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District of Columbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NE': 'Nebraska',
    'NH': 'New Hampsire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'PR': 'Puerto Rico',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virgina',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virgina',
    'WY': 'Wyoming'
}

def determine_search_terms(request, state_param):
    #if we got actual params, just use those
    if request.GET.get('q') or request.GET.get('l'):
        return
    state_name = state_param.lower()
    if state_name is None:
        return

    request.GET = request.GET.copy()
    if state_name in states_name_to_codes:
        state_code = states_name_to_codes[state_name]
        request.GET['q'] = ''
        request.GET['l'] = state_code
        return
    else:
        request.GET['404'] = True
        return