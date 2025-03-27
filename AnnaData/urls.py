from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from api.models import CropResource, IntercroppingDataResource

crop_resource = CropResource()
intercropping_data_resource = IntercroppingDataResource()


urlpatterns = [
    path('',views.index, name='index'),
    path('admin/', admin.site.urls),
    path('AboutUs/', include('AboutUs.urls')),    
    path('Crop/', include('Crops.urls')),
    path('ImageRecog/', include('ImageRecog.urls')),
    path('MixedFarming/', include('MixedFarming.urls')),
    path('api/intercropping', include(intercropping_data_resource.urls)),
    path('api/crop', include(crop_resource.urls)),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
