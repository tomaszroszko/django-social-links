from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _


class SocialLinkType(models.Model):
    """
    Define Link Types possible to use. For example: facebook, twitter...
    Allow to upload icon or insert css class
    """

    name = models.CharField(_('Name'), max_length=50)
    css_class = models.CharField(_('Css class'), max_length=50, null=True,
                                 blank=True)
    image = models.ImageField(upload_to='sociallinks/', null=True, blank=True)

    class Meta:
        verbose_name = _('Social link type')
        verbose_name_plural = _('Social link types')
        ordering = ('name',)

    def __unicode__(self):
        return self.name


class SocialLinkGroup(models.Model):
    """Group of link that you can place in diffrent part of app/web and
    assing social link to it"""

    name = models.CharField(_('Name'), max_length=50)
    slug = models.SlugField(_('Slug'), max_length=50, unique=True)

    class Meta:
        verbose_name = _('Link Group')
        verbose_name_plural = _('Link Groups')
        ordering = ('name',)

    def __unicode__(self):
        return self.name


class SocialLink(models.Model):
    """
    Social Link possible to use with relation to
    SocialGroup or any object from INSTALLED APPS
    """

    link_type = models.ForeignKey(SocialLinkType)
    link_group = models.ForeignKey(SocialLinkGroup, null=True, blank=True)
    content_type = models.ForeignKey(ContentType, null=True, blank=True)
    object_pk = models.IntegerField(_('Object pk'), null=True, blank=True)
    link = models.URLField(_('Link'))
    priority = models.PositiveSmallIntegerField(_('Priority'), default=0)

    class Meta:
        verbose_name = _('Social Link')
        verbose_name_plural = _('Social Links')
        ordering = ('priority',)

    def __unicode__(self):
        return self.link
