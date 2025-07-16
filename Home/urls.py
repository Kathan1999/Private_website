from Home import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('home/projectpost/<slug:slug>/', views.projectpost, name="projectpost"),
]
