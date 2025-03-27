from django.contrib import admin
from django.utils.html import format_html
from .models import Crop
# Register your models here.


class CropAdmin(admin.ModelAdmin):
    list_display=('id','display_image','name','Soil','nutrition','fertilizer','MSP')
    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{0}" width="150" height="225" />', obj.image.url)
        return "No Image"

    display_image.short_description = 'Image'

admin.site.register(Crop,CropAdmin)
