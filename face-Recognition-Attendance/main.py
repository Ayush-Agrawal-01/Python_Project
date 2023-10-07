# In Terminal :-
 #pip install face_recognition
 #pip install cmake
 #pip install opencv-python
 #pip install numpy

import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

video_capture = cv2.VideoCapture(0)

# load known faces
Ayush_image = face_recognition.load_image_file("faces/Ayush.jpg")
Ayush_encoding = face_recognition.face_encodings(Ayush_image)[0]

Harry_image = face_recognition.load_image_file("faces/Harry.jpg")
Harry_encoding = face_recognition.face_encodings(Harry_image)[0]

known_face_encoding = [Ayush_encoding, Harry_encoding]
known_face_namse = ["Ayush", "Harry"]

# list of excepted students
students = known_face_names.copy()

face_locations = []
face_encodings = []

# get the current date and time
now = datetime.now()
current_date = now.strftime("%y-%m-%d")

f = open(f"{current_date}.csv", "w+", newline='')
lnwriter = csv.writer(f)

while True:
