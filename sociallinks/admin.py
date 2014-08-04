from django.contrib import admin
from .models import SocialLinkGroup, SocialLink, SocialLinkType


class SocialLinkTypeAdmin(admin.ModelAdmin):
    pass


class SocialLinkAdmin(admin.ModelAdmin):
    model = SocialLink
    fields = ('link_type', 'link', 'priority', 'content_type', 'object_pk')
    related_lookup_fields = {
        'generic': (('content_type', 'object_pk'),)
    }


class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    fields = ('link_type', 'link_group', 'link', 'priority')
    sortable_field_name = "priority"
    extra = 0


class SocialLinkGroupAdmin(admin.ModelAdmin):
    inlines = (SocialLinkInline,)


admin.site.register(SocialLinkType, SocialLinkTypeAdmin)
admin.site.register(SocialLinkGroup, SocialLinkGroupAdmin)
admin.site.register(SocialLink, SocialLinkAdmin)
