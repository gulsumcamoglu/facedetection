from django.urls import path
from django.shortcuts import render
from django.http import HttpResponse
from facedetection.views import detectPersons,detections,addPerson,dailyReport



urlpatterns = [
    path('detectPersons/', detectPersons, name='detectPersons'),
    path('addPerson/', addPerson, name='addPerson'),
    path('detections/', detections, name='detections'),
    path('dailyReport/', dailyReport, name='dailyReport'),
]
