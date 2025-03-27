from django.contrib import admin
from .models import IntercroppingData, CompanionCrop, CroppingPattern

class CompanionCropAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class CroppingPatternAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class IntercroppingDataAdmin(admin.ModelAdmin):
    list_display = ('primary_crop', 'get_companion_crops', 'brief_benefits', 'main_crop_percentage','companion_crop_percentage')
    search_fields = ('primary_crop', 'benefits')
    filter_horizontal = ('companion_crops','patterns')

    def get_companion_crops(self, obj):
        return ", ".join([crop.name for crop in obj.companion_crops.all()])
    get_companion_crops.short_description = 'Companion Crops'
    
    def brief_benefits(self, obj):
        return obj.benefits[:50] + '...' if len(obj.benefits) > 50 else obj.benefits
    brief_benefits.short_description = 'Benefits'

admin.site.register(CompanionCrop, CompanionCropAdmin)
admin.site.register(CroppingPattern, CroppingPatternAdmin)
admin.site.register(IntercroppingData, IntercroppingDataAdmin)