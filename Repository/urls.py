from django.urls import path
from . import views

app_name = 'Repository'

urlpatterns = [
    path('repository', views.repo_list),
    path('repository/latest', views.latest_repo_list)
]