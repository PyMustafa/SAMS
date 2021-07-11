from .models import Image, Flag
import base64
import pickle
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


# pip install opencv-python

@receiver(post_save, sender=Image)
def job(sender, **kwargs):
    print("the job started ..............")
    images = []
    stdID = []
    encodeList = []

    data = Image.objects.values('student_id', 'student_image')

    for img in data:
        images.append(img['student_image'])
    for iid in data:
        stdID.append(iid['student_id'])

    for IMG in images:
        Bufferimage = 'examble.jpg'
        IMG = bytes(IMG, 'utf-8')

        print(type(IMG))
        with open(Bufferimage, 'wb') as f:
            print("test0 -------")
            f.write(base64.b64decode(IMG))
            print("test1 -------")
        print("test2 -------")
        curimage = cv2.imread(Bufferimage)
        print("test3 -------")
        img = cv2.cvtColor(curimage, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        print("test4 -------")
        encodeList.append(encode)
        print("test5 -------")

    with open("IMGEncode.txt", "wb") as fp:
        pickle.dump(encodeList, fp)
    with open("StudentTD.txt", "wb") as fp:
        pickle.dump(stdID, fp)
