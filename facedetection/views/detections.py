from django.http import HttpResponse
from django.shortcuts import render

def detections(request):
    return render(request,'pages/detections.html',context={})