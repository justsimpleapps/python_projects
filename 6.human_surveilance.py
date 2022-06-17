import cv2, time
from datetime import datetime
import argparse
import os

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

video=cv2.VideoCapture(0)

while True:
    check,frame=video.read()
    if frame is not None:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray,scale=1.1,minNeighbours=10)
        from x,y,w,h in faces:
        img=cv2.rectangle




