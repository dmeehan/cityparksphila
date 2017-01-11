from __future__ import absolute_import, unicode_literals

from django.db import models


from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, PageChooserPanel, StreamFieldPanel
from wagtail.wagtailcore.blocks import StreamBlock, CharBlock, RichTextBlock, PageChooserBlock
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index


from modelcluster.fields import ParentalKey

from core.blocks import PullQuoteBlock, ImageBlock, LinkBlock

class HomePageStreamBlock(StreamBlock):
    h2 = CharBlock(icon="title", classname="title")
    h3 = CharBlock(icon="title", classname="title")
    h4 = CharBlock(icon="title", classname="title")
    intro = RichTextBlock(icon="pilcrow")
    paragraph = RichTextBlock(icon="pilcrow")
    aligned_image = ImageBlock(label="Aligned image", icon="image")
    pullquote = PullQuoteBlock()
    link = LinkBlock()

class HomePageGalleryItem(Orderable):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+',
        help_text='Add if you want this item to link to a page on this site.'
    )
    caption = models.CharField(max_length=255, blank=True)
    page = ParentalKey('home.HomePage', related_name='banner_items')

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
        PageChooserPanel('link_page'),
    ]

class HomePage(Page):
    body = StreamField(HomePageStreamBlock())
    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    class Meta:
        verbose_name = "Homepage"

HomePage.content_panels = [
    FieldPanel('title', classname="full title"),
    InlinePanel('banner_items', label="Banner items"),
    StreamFieldPanel('body'),
]

HomePage.promote_panels = Page.promote_panels