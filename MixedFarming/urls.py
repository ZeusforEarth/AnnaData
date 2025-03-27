from django.urls import path, include
from . import views

app_name = 'MixedFarming'
urlpatterns = [
    path('',views.index,name='index'),
    path('intercropping/', views.search_intercropping, name='intercropping_search'),
]
