from django.shortcuts import render
from django.db.models import Q
from .models import IntercroppingData, CompanionCrop

def search_intercropping(request):
    query = request.GET.get('search', '')
    
    if query:
        # Search for intercropping data based on the primary crop or companion crop
        results = IntercroppingData.objects.filter(
            Q(primary_crop__icontains=query) | 
            Q(companion_crops__name__icontains=query)
        ).distinct()
    else:
        results = []
    
    return render(request, 'MixedFarming/plantpartnerout.html', {'query': query,'results': results})

# Create your views here.
def index(request):
    return render(request, 'MixedFarming/plantpartnerint.html')



