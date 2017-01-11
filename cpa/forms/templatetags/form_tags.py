from django import template

from ..models import FormPage

register = template.Library()

@register.inclusion_tag('forms/_form.html')
def form(slug):
    form_page = FormPage.objects.get(slug=slug)
    form = form_page.get_form()
    return {'form_page': form_page, 'form': form}