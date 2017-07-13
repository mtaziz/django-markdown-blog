from urllib import parse

from django import template


register = template.Library()


@register.simple_tag
def urljoin(base, path):
    return parse.urljoin(base, path)
