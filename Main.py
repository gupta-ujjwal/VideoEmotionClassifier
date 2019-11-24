import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
from keras.models import load_model
from keras.preprocessing.image import img_to_array

width=130 #you can change this in a multiple of 2
height=86
Emotions = [(0,'Angry'),(1,'Fear'),(2,'Sad'),(3,'Happy'),(4,'Neutral'),(5,'Surprised')]
face_cascade = cv2.CascadeClassifier('FaceDetectionXML/frontface_alt.xml')
eye_cascade = cv2.CascadeClassifier('FaceDetectionXML/eye.xml')

#Load the model 
model = load_model('model.h5')
print('Model Loaded')


Data = []
AngryData = []
FearData = []
SadData = []
HappyData = []
NeutralData = []
SurprisedData = []

flag = 0
i=0

name = 'Test4.mp4'

# Opens the Video file
cap= cv2.VideoCapture(name)
print('------------------------------------------------------')
print('Reading Video -',name)
print('------------------------------------------------------')

#Calculating FPS
# Find OpenCV version
(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

if int(major_ver)  < 3 :
    fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
else :
    fps = cap.get(cv2.CAP_PROP_FPS)
    
fps = int(fps)
print('FPS of video -',fps)

while(cap.isOpened()):
    ret, frame = cap.read()
    if i%fps == 0:
        if ret == False:
            break
        img = frame
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        margin = 30
        faces = face_cascade.detectMultiScale(gray, 1.3, 3)
        for (x,y,w,h) in faces:
            flag = 1
            croppedFace = img[y-margin-10:y+h+margin+10, x-margin:x+w+margin]
                    
        if len(faces):
            finalImage=cv2.resize(croppedFace,(width ,height))
            image = finalImage.astype("float") / 255.0
            image = img_to_array(image)
            image = np.expand_dims(image, axis=0)
            arr = model.predict(image)[0]
            AngryData.append(arr[0])
            FearData.append(arr[1])
            SadData.append(arr[2])
            HappyData.append(arr[3])
            NeutralData.append(arr[4])
            SurprisedData.append(arr[5])
            EmotionIndex, = np.where(arr == max(arr))
            tu = (i,Emotions[EmotionIndex[0]][1])
            Data.append(tu)
    i+=1

cap.release()
cv2.destroyAllWindows()


print('Processing Complete')

if not flag: 
    print('Can not detect faces')
else:
    print('The emotions expressed over time in the video are:') 
    for i in Data:
        print('Time -',i[0]/fps,' Emotion - ',i[1])
    
    print('Scores for each reaction for the video are :')
    #Plotting each reaction scores
    fig, ax = plt.subplots(nrows=3,ncols=2, figsize=(10,10))
    ax[0][0].plot(AngryData)
    ax[0][0].set_title("Angry Score")
    
    ax[0][1].plot(FearData)#row=0, col=1
    ax[0][1].set_title("Fear Score")
    
    ax[1][0].plot(SadData)
    ax[1][0].set_title("Sad Score")
    
    ax[1][1].plot(HappyData)
    ax[1][1].set_title("Happy Score")
    
    ax[2][0].plot(NeutralData)
    ax[2][0].set_title("Neutral Score")
    
    ax[2][1].plot(SurprisedData)
    ax[2][1].set_title("Surprised Score")
    
    
    plt.show()
print('-------------------------------------------------------------------------------------------')
