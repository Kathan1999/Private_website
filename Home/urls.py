from Home import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('projectpost', views.ProjectPost, name="ProjectPost"),
]
