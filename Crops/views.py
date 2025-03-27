from django.shortcuts import render
from .models import Crop

# Create your views here.
def index(request):
    Crops = Crop.objects.all()
    return render(request, 'Crops/crop_index.html', {'Crops': Crops})

def detail(request,crop_name):
    crop = Crop.objects.get(name=crop_name)
    return render(request, 'Crops/crop_detail.html', {'crop': crop})