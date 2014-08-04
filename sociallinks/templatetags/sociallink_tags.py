# -*- coding: utf-8 -*-

from django import template
from django.contrib.contenttypes.models import ContentType
from sociallinks.models import SocialLink, SocialLinkGroup

register = template.Library()


@register.assignment_tag
def obj_social_links(obj):
    """return list of social links for obj. Obj is instance of any model
    registred in project

    Usage:
    {% obj_social_links user as user_links %}
    {% for link in user_links %}
        <a href="{{ link.link }}" class="{{ link.link_type.css_class }}">
            {{ link.link_type.name }}
        </a>
    {% endfor %}

    """
    content_type = ContentType.objects.get_for_model(obj.__class__)
    return SocialLink.objects.filter(
        content_type=content_type,
        object_pk=obj.pk).select_related('link_type')


@register.assignment_tag
def group_social_links(slug):
    """return list of social links for slug
    sociallinks.models.SocialLinkGroup.slug"""

    group = SocialLinkGroup.objects.get(slug=slug)
    return SocialLink.objects.filter(
        link_group=group)


