#!/usr/bin/env python
#:coding=utf-8:
#:tabSize=2:indentSize=2:noTabs=true:
#:folding=explicit:collapseFolds=1:

# Code copied from:
# http://w.holeso.me/2008/08/a-simple-django-truncate-filter/

from django import template
register = template.Library()

@register.filter
def truncate_chars(value, max_length):
  if value is not None:
    if len(value) > max_length:
      truncd_val = value[:max_length]
      truncd_val = truncd_val.rstrip()
      return  truncd_val + "..."
  return value
