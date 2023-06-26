from django.contrib import admin
from django.utils.html import format_html

from .models import Project, Tag, PhotoSource, Recipient, DynamicParam
from django.conf import settings

admin.site.register(Tag)


@admin.register(PhotoSource)
class PhotoSource(admin.ModelAdmin):
    list_display = ("display_image", "name", "created_at")

    readonly_fields = ('display_image',)  # Add the image field to the read-only fields

    def display_image(self, obj):
        # Generate the HTML to display the image
        return format_html(f'<img src="{obj.photo.url}" width="100" height="100" />')

    display_image.short_description = 'Image'



@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("display_image", "name", "season", "year", "city")

    readonly_fields = ('display_image',)  # Add the image field to the read-only fields

    def display_image(self, obj):
        # Generate the HTML to display the image
        return format_html(f'<img src="{obj.photo.url}" width="100" height="100" />')

    display_image.short_description = 'Image'


@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ("email",)


@admin.register(DynamicParam)
class DynamicAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "value")
