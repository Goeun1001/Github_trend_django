from django.urls import path
from . import views

app_name = 'Topic'

urlpatterns = [
    path('topic', views.topic_list),
    path('topic/lang', views.topic_detail),
]