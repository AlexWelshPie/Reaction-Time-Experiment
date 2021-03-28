from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name='patterns-home'),
    path("about", views.about, name='patterns-about'),
    path("pygalexample", views.pygalexample, name='patterns-pygalexample'),
    path("bubbleChart9", views.bubbleChart9, name='patterns-bubbleChart9'),
    path("bubble25", views.bubble25, name='patterns-bubble25'),
    path("bubble5", views.bubble5, name='patterns-bubble5'),
    path("text3", views.text3, name='patterns-text3'),
    path("text5", views.text5, name='patterns-text5'),
    path("text9", views.text9, name='patterns-text9'),
    path("text25", views.text25, name='patterns-text25'),
]