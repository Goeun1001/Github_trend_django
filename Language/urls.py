from django.urls import path
from . import views

app_name = 'Language'

urlpatterns = [
    path('language', views.language_list),
    path('language/search', views.language_search),
    path('language/repo', views.language_repo),
]