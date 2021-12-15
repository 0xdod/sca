from django import template

register = template.Library()


@register.filter(name='addattr')
def addattr(value, attrs):
    return value.as_widget(attrs=attrs)


@register.simple_tag(name='dict')
def Dict(*args):
    d = {}
    for i in range(0, len(args), 2):
        if i + 1 < len(args):
            d[args[i]] = args[i+1]

    return d
