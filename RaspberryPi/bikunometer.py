import firebase_admin
from firebase_admin import credentials, storage, db
import numpy as np
import cv2
import time
import datetime

from tflite_support.task import core
from tflite_support.task import processor
from tflite_support.task import vision
import utils

model='efficientdet_lite0.tflite'
num_threads=4

dispW=1280
dispH=720

fpos=(dispW-150,60)
font=cv2.FONT_HERSHEY_SIMPLEX
fheight=1.5
fweight=3
fcolor=(255,0,0)

fposcount=(20,60)

labelHeight=1.5
labelColor=(0,255,0)
labelWeight=(2)

boxColor=(255,0,0)
boxWeight=2

cred = credentials.Certificate("bikunometer-6a9b1-firebase-adminsdk-k4wlj-297cd578d8.json")
firebase_admin.initialize_app(cred,{
    'storageBucket':'bikunometer-6a9b1.appspot.com',
    'databaseURL' : 'https://bikunometer-6a9b1-default-rtdb.asia-southeast1.firebasedatabase.app'
    })


base_options=core.BaseOptions(file_name=model,use_coral=False,num_threads=num_threads)
detection_options=processor.DetectionOptions(max_results=20, score_threshold= .3)
options=vision.ObjectDetectorOptions(base_options=base_options, detection_options=detection_options)
detector=vision.ObjectDetector.create_from_options(options)

checkphoto= 0

while True:
    current_datetime = datetime.datetime.now()
    formated_date = current_datetime.strftime("%Y-%m-%d")
    formated_time = current_datetime.strftime("%H:%M")
    year = current_datetime.year
    month = current_datetime.month
    day = current_datetime.day
    hour = current_datetime.hour
    minute = current_datetime.minute
    second = current_datetime.second
    
    print('Hour : ',hour)

    if (hour >=6) and (hour < 21):
        if (minute%2 == 0) and (checkphoto ==0):    
            checkphoto = 1;
            bucket = storage.bucket()
            blob = bucket.get_blob("data/photo.jpg")
            ref = db.reference('/Halte-FT')
            print ('bucket',bucket)
            print ('blob',blob)

            #ret, im = cam.read()
            #im=picam2.capture_array()
            #im=cv2.flip(im,-1)
            arr = np.frombuffer(blob.download_as_string(), np.uint8)
            im = cv2.imdecode(arr, cv2.COLOR_BGR2BGR555)
            
            imRGB=cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
            imTensor=vision.TensorImage.create_from_array(imRGB)
            myDetects=detector.detect(imTensor)
            print()
            person = 0;
            bus = 0;
            for myDetect in myDetects.detections:
                UL=(myDetect.bounding_box.origin_x, myDetect.bounding_box.origin_y)
                LR=(myDetect.bounding_box.origin_x+myDetect.bounding_box.width,myDetect.bounding_box.origin_y+myDetect.bounding_box.height)
                objName=myDetect.categories[0].category_name
                if objName=="person":
                    im=cv2.rectangle(im,UL,LR, boxColor,boxWeight)
                    cv2.putText(im,objName,UL,font,labelHeight,labelColor, labelWeight)
                    person=person+1
                if objName=="bus":
                    bus=1
            
            ref = db.reference('/Halte-FT/'+formated_date+'/'+formated_time)
            data = {"Person" : person, "Bus": bus}
            ref.set(data)    

            cv2.putText(im,'Person : '+str(int(person)),fposcount,font,fheight,fcolor,fweight)
            cv2.imshow('Photo Halte', im)
            print("Person : ", str(int(person)))
            print("Bus    : ", str(int(bus)))
        elif (minute%2 == 1):
            checkphoto = 0;  
            print("ganjil...")
        time.sleep(30)
    
    if cv2.waitKey(1)==ord('q'):
        break
    
cv2.destroyAllWindows()

