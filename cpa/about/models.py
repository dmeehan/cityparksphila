from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, PageChooserPanel, StreamFieldPanel
from wagtail.wagtailcore.blocks import StreamBlock, CharBlock, RichTextBlock
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index


from modelcluster.fields import ParentalKey

from core.blocks import PullQuoteBlock, ImageBlock

class AboutPageStreamBlock(StreamBlock):
    h2 = CharBlock(icon="title", classname="title")
    h3 = CharBlock(icon="title", classname="title")
    h4 = CharBlock(icon="title", classname="title")
    intro = RichTextBlock(icon="pilcrow")
    paragraph = RichTextBlock(icon="pilcrow")
    aligned_image = ImageBlock(label="Aligned image", icon="image")

class AboutPage(Page):
    body = StreamField(AboutPageStreamBlock())
    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

AboutPage.content_panels = [
    FieldPanel('title', classname="full title"),
    StreamFieldPanel('body'),
]
