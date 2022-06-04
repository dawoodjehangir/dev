from django.urls import path

# grab all the views from view.py inside the api directory, that's why we have . there
from . import views


urlpatterns = [
    path('', views.api_home)
]