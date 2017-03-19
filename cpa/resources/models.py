from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.models import ContentType

from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager
from taggit.models import Tag, TaggedItemBase

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index


class ResourcesIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    class Meta:
        verbose_name = "Resources Index Page"

    def get_context(self, request):
        # Update context to include only published resources, ordered by reverse-chron
        context = super(ResourcesIndexPage, self).get_context(request)
        resourcepages = self.get_children().live().order_by('-first_published_at')
        context['resourcepages'] = resourcepages
        return context

class ResourcePageTag(TaggedItemBase):
    content_object = ParentalKey('ResourcePage', related_name='tagged_items')


class ResourcePage(Page):
    intro = models.CharField(max_length=255, blank=True)
    link = models.URLField(blank=True)
    publication = models.CharField(max_length=255, blank=True)
    date = models.DateField("Publication Date", blank=True, null=True)
    description = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=ResourcePageTag, blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('description'),
        index.SearchField('publication'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('link'),
        FieldPanel('publication'),
        FieldPanel('date'),
        FieldPanel('description'),
        FieldPanel('tags'),
    ]

class ResourceTagIndexPage(Page):

    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        resourcepages = ResourcePage.objects.filter().filter(tags__name=tag)

        # Update template context
        context = super(ResourceTagIndexPage, self).get_context(request)
        context['resourcespages'] = resourcepages
        return context
