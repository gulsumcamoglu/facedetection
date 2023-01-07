from django.shortcuts import render
from facedetection.models import detectionModel
def detections(request):
    detections = detectionModel.objects.all()
    return render(request,'pages/detections.html',context={
        'detections' : detections
    })