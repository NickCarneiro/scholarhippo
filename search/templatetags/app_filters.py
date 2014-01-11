from django import template
from datetime import date, timedelta
from search.request_utils import states_codes_to_names

register = template.Library()

@register.filter(name='pretty_state')
def pretty_state(state_code):
    if state_code in states_codes_to_names:
        return states_codes_to_names[state_code]
    else:
        raise Exception('Unknown state code {}'.format(state_code))