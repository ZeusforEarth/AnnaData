from django.db import models

# Create your models here.


class CompanionCrop(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class CroppingPattern(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class IntercroppingData(models.Model):
    primary_crop = models.CharField(max_length=100)
    companion_crops = models.ManyToManyField(CompanionCrop, related_name='intercropping_data')
    patterns = models.ManyToManyField(CroppingPattern, related_name='intercropping_pattern')
    companion_crop_percentage = models.FloatField(default=0)
    @property
    def main_crop_percentage(self):
       return 100 - self.companion_crop_percentage
    benefits = models.TextField()
    
    def get_companion_crops_list(self):
        return ", ".join(crop.name for crop in self.companion_crops.all())
    
    def __str__(self):
        return f"{self.primary_crop} Intercropping"