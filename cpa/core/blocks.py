import markdown

from django import forms
from django.db import models

from wagtail.wagtailadmin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.wagtailcore.blocks import TextBlock, StructBlock, StreamBlock, FieldBlock, CharBlock, RichTextBlock, RawHTMLBlock, PageChooserBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtaildocs.blocks import DocumentChooserBlock

class LinkBlock(StructBlock):
    text = CharBlock()
    page = PageChooserBlock()

    class Meta:
        icon = "link"


class PullQuoteBlock(StructBlock):
    quote = TextBlock("quote title")
    attribution = CharBlock()

    class Meta:
        icon = "openquote"


class ImageFormatChoiceBlock(FieldBlock):
    field = forms.ChoiceField(choices=(
        ('left', 'Wrap left'), ('right', 'Wrap right'), ('mid', 'Mid width'), ('full', 'Full width'),
    ))


class HTMLAlignmentChoiceBlock(FieldBlock):
    field = forms.ChoiceField(choices=(
        ('normal', 'Normal'), ('full', 'Full width'),
    ))


class ImageBlock(StructBlock):
    image = ImageChooserBlock()
    caption = RichTextBlock()
    alignment = ImageFormatChoiceBlock()


class AlignedHTMLBlock(StructBlock):
    html = RawHTMLBlock()
    alignment = HTMLAlignmentChoiceBlock()

    class Meta:
        icon = "code"

class MarkDownBlock(TextBlock):
    """
    A MarkDown block for Wagtail streamfields.
    """

    class Meta:
        icon = 'pilcrow'

    def render_basic(self, value):
        md = markdown(
            value,
            [
                'markdown.extensions.fenced_code',
                'codehilite',
            ],
        )
        return mark_safe(md)
