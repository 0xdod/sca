from django import template

register = template.Library()


@register.simple_tag
def call_method(obj, method_name, *args):
    try:
        method = getattr(obj, method_name)
        return method(*args)
    except AttributeError:
        pass
