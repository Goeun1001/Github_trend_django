from django.urls import path

from . import views

app_name = 'JSON'

urlpatterns = [
    path('getJson', views.getJson),
    path('years', views.getYear),
]
