# contact/templatetags/contact_tags.py

from django import template
register = template.Library()

@register.inclusion_tag('contact/includes/contact_form.html')
def contact_form():
    form = ContactForm()
    return {'form': form}