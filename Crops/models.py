from django.db import models

# Create your models here.


class Crop(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='crop_images/')  # Requires Pillow library
    Soil = models.CharField(max_length=500)
    nutrition = models.CharField(max_length=500)
    fertilizer = models.CharField(max_length=500)
    MSP = models.CharField(max_length=50)

    def __str__(self):
        return self.name
