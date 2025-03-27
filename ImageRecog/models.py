import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from gpt4all import GPT4All
from django.db import models

class PestDiseaseAnalysis(models.Model):
    image = models.ImageField(upload_to='plant_images/')
    detected_issue = models.CharField(max_length=200, blank=True, null=True)
    analysis_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Analysis of {self.image.name} on {self.analysis_date}"