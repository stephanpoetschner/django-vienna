# -*- coding: utf-8 -*-
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='image')
def image(value):
    if not value:
        return u''

    return mark_safe(u'<img src="%(url)s" width="%(width)s" ' \
        u'height="%(height)s" alt="%(alt)s" title="%(title)s">' % value)
