from django.urls import path, include
from . import views

app_name = 'AboutUs'
urlpatterns = [
    path('',views.index,name='index'),
]
