from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name='patterns-home'),
    path("about", views.about, name='patterns-about'),
    path("pygalexample", views.pygalexample, name='patterns-about'),
]