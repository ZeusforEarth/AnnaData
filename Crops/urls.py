from django.urls import path, include
from . import views

app_name = 'Crops'
urlpatterns = [
    path('',views.index,name='index'),
    path('<str:crop_name>/',views.detail,name='crop_detail'),
]
