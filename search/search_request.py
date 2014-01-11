class SearchRequest:
    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
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
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
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
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }
    def __init__(self, keyword="", location="", no_essay_required=False,
                 deadline=None,
                 ethnicity_restriction=None,
                 gender_restriction=None):
        self.location = location
        self.keyword = keyword
        self.no_essay_required = no_essay_required
        self.deadline = deadline
        self.ethnicity_restriction = ethnicity_restriction
        self.gender_restriction = gender_restriction

    def get_base_url(self, start):
        url = '/search?q=' + self.keyword
        if self.location is not None:
            url += '&l=' + self.location
        if self.no_essay_required:
            url += '&ne=true'
        if self.deadline is not None:
            url += '&d=' + self.deadline
        if self.ethnicity_restriction is not None:
            url += '&e=' + str(self.ethnicity_restriction)
        if self.gender_restriction is not None:
            url += '&g=' + str(self.gender_restriction)
        if start is not None and start > 0:
            url += '&start=' + str(start)
        return url

    def get_canonical_url(self, keyword, location):
        if keyword == "" and (location == "" or location == "US"):
            return "/no-essay-scholarships"

        if keyword == "" and location in self.states:
            return "/scholarships-in-" + str.lower(self.states[location]).replace(' ', '-')
        return None