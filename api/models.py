from django.db import models
from tastypie.resources import ModelResource
from Crops.models import Crop
from MixedFarming.models import  IntercroppingData

# Create your models here.

class CropResource(ModelResource):
    class Meta:
        queryset = Crop.objects.all()
        resource_name = 'crop'
        fields = ['id', 'name', 'description', 'image']

class IntercroppingDataResource(ModelResource):
    class Meta:
        queryset = IntercroppingData.objects.all()
        resource_name='intercropping_data'
        fields = ['id', 'primary_crop', 'companion_crops', 'patterns', 'companion_crop_percentage', 'main_crop_percentage', 'benefits']