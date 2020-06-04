from django import template

register = template.Library()


@register.filter
def range_color(value):
    color = ''
    if value == '' or value == '-':
        value = 0
    percent = float(value)
    if percent < 0:
        color = 'MediumSpringGreen'
    elif 0 < percent < 1:
        color = 'white'
    elif 1 < percent < 2:
        color = 'pink'
    elif 2 < percent < 5:
        color = 'LightCoral'
    elif percent >= 5:
        color = 'red'
    return color


@register.filter
def null_value(value):
    if value == '':
        res = '-'
    else:
        res = value
    return res
