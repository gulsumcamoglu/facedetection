from django.http import HttpResponse
from facedetection.models import detectionModel
from django.shortcuts import render,redirect
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
from datetime import date
import time

def detectPersons(request):
    
    if request.method =='POST':
        id,name,day,time = takeImage()
        detection = detectionModel()
        detection.image = os.path.join('C:/Users/acer/Desktop/FaceDetection/media/uploads/'+str(name)+'.'+str(id)+'.jpg')
        detection.name = name
        detection.id = id
        detection.date = day
        detection.time =time
        detection.save()

        return redirect('detectPersons') 
        
             
    return render(request,'pages/detectPerson.html',context={})

def takeImage():
    count = 0
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        facetracker = load_model('facedetection/facetracker.h5') 

        r = cv2.face.LBPHFaceRecognizer_create()
        r.read('facedetection\model.yml')
        names = ['','Yakup','Gulsum','Esra','Hasan'] 
        _ , frame = cap.read()
        frame = frame[50:500, 50:500,:]
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        resized = tf.image.resize(rgb, (120,120))
        
        yhat = facetracker.predict(np.expand_dims(resized/255,0))
        sample_coords = yhat[1][0]
        print(np.multiply(sample_coords, [450,450,450,450]).astype(int))
        
        for [x,y,w,h] in [np.multiply(sample_coords, [450,450,450,450]).astype(int).tolist()]:
            
            if x > 10:
                id, confidence = r.predict(gray[y:h,x:w])
                idNum = id
                print(confidence)
                cv2.rectangle(frame, 
                            tuple(np.multiply(sample_coords[:2], [450,450]).astype(int)),
                            tuple(np.multiply(sample_coords[2:], [450,450]).astype(int)), 
                                    (255,0,0), 2)
                # Controls the label rectangle
                cv2.rectangle(frame, 
                            tuple(np.add(np.multiply(sample_coords[:2], [450,450]).astype(int), 
                                            [0,-30])),
                            tuple(np.add(np.multiply(sample_coords[:2], [450,450]).astype(int),
                                            [80,0])), 
                                    (255,0,0), -1)
                if  yhat[0] > 0.5  and confidence<84: 
                    id = names[id]
                # Controls the text rendered
                    cv2.putText(frame, str(id), tuple(np.add(np.multiply(sample_coords[:2], [450,450]).astype(int),
                            [0,-5])),cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
                else:
                    id = "unknown"
                    cv2.putText(frame, str(id), tuple(np.add(np.multiply(sample_coords[:2], [450,450]).astype(int),
                            [0,-5])),cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
            else:
                id = "no face"
                cv2.putText(frame, str(id), tuple(np.add(np.multiply(sample_coords[:2], [450,450]).astype(int),
                                [0,-5])),cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
        

        
        
        cv2.imshow('EyeTrack', frame)
        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            lastId = ""
            lastName = ""
            today = date.today() #for finding the day
            t = time.localtime() 

            # SPACE pressed
            
            file_name_path2 = 'C:/Users/acer/Desktop/FaceDetection/media/uploads/'+str(id)+'.'+str(idNum)+'.jpg'
            lastId= idNum
            lastName = id
            
            cv2.imwrite(file_name_path2, frame)
            print("{} written!".format(file_name_path2))
            d1 = today.strftime("%d/%m/%Y")
            current_time = time.strftime("%H:%M:%S", t)
            cap.release()
            cv2.destroyAllWindows()
            return lastId,lastName,d1,current_time
    
    
        

    


