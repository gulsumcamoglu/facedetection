from django.shortcuts import render
from facedetection.models import reportModel
def dailyReport(request):
    
    return render(request,'pages/dailyReport.html',context={
        
    })