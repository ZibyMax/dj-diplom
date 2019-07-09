from django import template

register = template.Library()


@register.filter
def rem_of_div(dividend, divider):
    return dividend % divider
