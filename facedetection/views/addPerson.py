from django.shortcuts import render,redirect
from facedetection.models import detectionModel
from django.contrib import messages
from facedetection.forms import takeId
import os
import time
import uuid
import cv2
from tensorflow.keras.models import load_model
import tensorflow as tf
import json
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import argparse
import imutils
id = 0
def addPerson(request):
    form = takeId()
    if request.method =='POST':
         form = takeId(request.POST)
         if form.is_valid():
             
             id = form.cleaned_data.get('id')
             #print(form.data['id']) 
             videoCapture(id) 
             
             context = {
                     'alert1':'trained'        
             }
             messages.add_message(request, messages.INFO, context['alert1'])
             
             faceSamples = []
             ids =[]
             imgPaths = [os.path.join('C:/Users/acer/Desktop/FaceDetection/dataset/',f) for f in os.listdir('C:/Users/acer/Desktop/FaceDetection/dataset/')]
             for i in imgPaths:
                img = Image.open(i)
                p_img = img.convert('L')
                img_numpy = np.array(p_img,'uint8')
                width,height = img.size
                id = int(os.path.split(i)[-1].split(".")[1])
                ids.append(id)
                    
                faceSamples.append(img_numpy[0:height,0:width])
                r = cv2.face.LBPHFaceRecognizer_create()
                r.train(faceSamples,np.array(ids))
                r.write("facedetection\model.yml")
             return redirect('addPerson')
             
           
       
              
    context = {
          'form':form          
    }
    return render(request,'pages/addPerson.html',context=context)

def videoCapture(id):
   count=0
   facetracker = load_model('facedetection/facetracker.h5') 
   cap = cv2.VideoCapture(0)
   cap.set(3, 640) # set video widht
   cap.set(4, 480)
   while cap.isOpened():
      _ , frame = cap.read()
    
      frame = frame[50:500, 50:500,:]
    
    
      rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
      resized = tf.image.resize(rgb, (120,120))
    
      yhat = facetracker.predict(np.expand_dims(resized/255,0))
      sample_coords = yhat[1][0]
      print(np.multiply(sample_coords, [450,450,450,450]).astype(int)) 
      for [x,y,w,h] in [np.multiply(sample_coords, [450,450,450,450]).astype(int).tolist()]:
          cv2.rectangle(frame, 
                          tuple(np.multiply(sample_coords[:2], [450,450]).astype(int)),
                          tuple(np.multiply(sample_coords[2:], [450,450]).astype(int)), 
                                (255,0,0), 2)
  
      
    
      
   
      if frame[y:h,x:w] is not None:
        count+=1
        face = cv2.resize(frame[y:h,x:w],(197,297))
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        
        file_name_path = 'C:/Users/acer/Desktop/FaceDetection/dataset/'+'User.'+str(id)+'.'+str(count)+'.jpg'
        print(file_name_path)
        cv2.imwrite(file_name_path,face)

        
        cv2.putText(face,str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
        cv2.imshow('Face Cropper',face)
      else:
        print("Face not found")
        pass

      if cv2.waitKey(1)==13 or count==5:
        break
    
   cap.release()
   cv2.destroyAllWindows()