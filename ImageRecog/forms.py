from django import forms
from .models import PestDiseaseAnalysis

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = PestDiseaseAnalysis
        fields = ['image']
        widgets = {
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
                'required': True
            })
        }