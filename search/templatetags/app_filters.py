from django import template
from search.request_utils import states_codes_to_names, encrypt_sid

register = template.Library()

@register.filter(name='pretty_state')
def pretty_state(state_code):
    if state_code in states_codes_to_names:
        return states_codes_to_names[state_code]
    else:
        raise Exception('Unknown state code {}'.format(state_code))

@register.filter
def id_to_key(value):
    return encrypt_sid(str(value))