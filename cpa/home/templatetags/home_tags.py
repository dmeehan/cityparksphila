from datetime import date
from django import template

from blog.models import BlogPage
from projects.models import ProjectPage

register = template.Library()

# Blog feed for home page
@register.inclusion_tag(
    'home/tags/blog_listing_homepage.html',
    takes_context=True
)

def blog_listing_homepage(context, count=3):
    blogpages = BlogPage.objects.live().order_by('-date')
    return {
        'blogpages': blogpages[:count],
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


# Blog feed for home page
@register.inclusion_tag(
    'home/tags/project_listing_homepage.html',
    takes_context=True
)

def project_listing_homepage(context, count=4):
    projects = ProjectPage.objects.live().order_by('-date')
    return {
        'projects': projects[:count],
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }