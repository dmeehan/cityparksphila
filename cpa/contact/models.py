
from django.db import models

from wagtail.wagtailadmin.edit_handlers import (FieldPanel, FieldRowPanel,
    InlinePanel, MultiFieldPanel)
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField

from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailforms.edit_handlers import FormSubmissionsPanel

from wagtail.contrib.settings.models import BaseSetting, register_setting

@register_setting
class ContactInformation(BaseSetting):
    title = models.CharField(max_length=255, blank=True)
    address_1 = models.CharField(max_length=255, blank=True)
    address_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    email = models.EmailField(blank=True,
        help_text='Email address to display on site.')
    phone = models.CharField(max_length=255, blank=True,
        help_text='Phone number to display on site.')


    panels = [
        FieldPanel('title'),
        FieldPanel('address_1'),
        FieldPanel('address_2'),
        FieldPanel('city'),
        FieldPanel('state'),
        FieldPanel('zip_code'),
        FieldPanel('email'),
        FieldPanel('phone'),
    ]