from django.urls import path
from . import views

app_name = 'ImageRecog'

urlpatterns = [
    path('', views.index, name='index'),
]