import mistune
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
@stringfilter
def markdown(value):
    return mark_safe(mistune.markdown(value, escape=False))


@register.filter
@stringfilter
def markdown_xhtml(value):
    return mistune.markdown(value, escape=False, use_xhtml=True)
