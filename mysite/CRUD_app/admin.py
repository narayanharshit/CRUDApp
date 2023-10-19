from django.contrib import admin
from .models import Item
from django.utils.html import format_html

# Register the Item model with the admin site.
admin.site.register(Item)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'display_image')

    def display_image(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.image.url)

    display_image.short_description = 'Image'