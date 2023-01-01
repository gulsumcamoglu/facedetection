from django.urls import path
from django.shortcuts import render
from django.http import HttpResponse
from facedetection.views import detectPersons,detections



urlpatterns = [
    path('detectPersons/', detectPersons),
    path('detections/', detections)
]
