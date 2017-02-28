from __future__ import unicode_literals

from django.db import models

from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index


class ProjectsIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    def get_context(self, request):
        # Update context to include only published projects, ordered by reverse-chron
        context = super(ProjectsIndexPage, self).get_context(request)
        projects = self.get_children().live().order_by('-first_published_at')
        context['projects'] = projects
        return context

class ProjectPageTag(TaggedItemBase):
    content_object = ParentalKey('ProjectPage', related_name='tagged_items')

class ProjectPage(Page):
    featured = models.BooleanField(default=False)
    date = models.DateField("Project date")
    intro = RichTextField(blank=True)
    description = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=ProjectPageTag, blank=True)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('description'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('featured'),
            FieldPanel('date'),
            FieldPanel('tags'),
        ], heading="Project information"),
        FieldPanel('intro'),
        FieldPanel('description'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]

class ProjectPageGalleryImage(Orderable):
    page = ParentalKey(ProjectPage, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]

class ProjectTagIndexPage(Page):

    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        projects = ProjectPage.objects.filter().filter(tags__name=tag)

        # Update template context
        context = super(ProjectTagIndexPage, self).get_context(request)
        context['projects'] = projects
        return context
