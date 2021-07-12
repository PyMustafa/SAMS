from .models import Image, Flag
from Lecture.models import CS1, Fourth_Year_Subjects, LectureSchedule
import pickle
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
import base64
import numpy


# receive the encodedImages from the server
# extract an encodeing for an image
# compare it with the encoding file
# then detect the identity of the image owner
@receiver(post_save, sender=Flag)
def job(sender, **kwargs):
    print("Test0 ---------------")
    encodedImages = []
    imageDate = []
    studentsIdWhoAttend = []
    with open("IMGEncode.txt", "rb") as fp:
        encodeListKnown = pickle.load(fp)

    with open("StudentTD.txt", "rb") as fp:
        StudentTD = pickle.load(fp)

    data = Image.objects.values('image', 'date')
    for img in data:
        encodedImages.append(img['image'])

    for iid in data:
        imageDate.append(iid['date'])
    count = 0

    for img in encodedImages:

        print("Test1 ---------------")
        image = 'image.jpg'
        img = bytes(img, 'utf-8')
        with open(image, 'wb') as f:
            f.write(base64.b64decode(img))

        rasp_StdImage_date = imageDate[count]
        count += 1
        print("Test2 ---------------")
        print("CurrentImg1 type")
        # print(type(image))
        CurrentImg = cv2.imread(image)
        CurrentImg = cv2.cvtColor(CurrentImg, cv2.COLOR_BGR2RGB)

        print("Test3 ---------------")
        print("CurrentImg1 type")
        print(type(CurrentImg))
        facesCurFrame = face_recognition.face_locations(CurrentImg)
        print("Test4 ---------------")
        if facesCurFrame:
            print("Test5 ---------------")
            encode = face_recognition.face_encodings(CurrentImg, facesCurFrame)
            print("Test6 ---------------")
            encode = numpy.array(encode)
            print("Test7 ---------------")
            faceDis = face_recognition.face_distance(encodeListKnown, encode)
            print("Test8 ---------------")
            matchIndex = np.argmin(faceDis)

            if faceDis[matchIndex] < 0.50:
                piStudentId = StudentTD[matchIndex].upper()

                # prevent registering attendance for one student more than onetime
                if piStudentId not in studentsIdWhoAttend:

                    print(piStudentId)
                    print(type(piStudentId))



                    day = int(rasp_StdImage_date[0:2])
                    month = int(rasp_StdImage_date[3:5])
                    year = int(rasp_StdImage_date[6:10])
                    houre = int(rasp_StdImage_date[12:14])
                    minut = int(rasp_StdImage_date[15:18])

                    if houre >= 9 and houre < 15:
                        studentsIdWhoAttend.append(piStudentId)
                        print("list of students how attend", studentsIdWhoAttend)


        #                 # x = CS1.objects.get(student_id=piStudentId)
        #                 # if x.week_1 != '-1':
        #                 #     if x.week_1 != '0':
        #                 #         x.week_1 = '1'
        #                 # elif x.week_2 != '1':
        #                 #     x.week_2 = '1'
        #                 # elif x.week_3 != '1':
        #                 #     x.week_3 = '1'
        #                 # elif x.week_4 != '1':
        #                 #     x.week_4 = '1'
        #                 # elif x.week_5 != '1':
        #                 #     x.week_5 = '1'
        #                 # elif x.week_6 != '1':
        #                 #     x.week_6 = '1'
        #                 # else:
        #                 #     x.week_7 = '1'
        #                 # x.save()
        #                 # print("attend save for: -",piStudentId )
        #
        #
        #
        #         # elif houre >= 10.3  and houre < 12:
        #         #     pass
        #         # elif houre >= 12  and houre < 1.3:
        #         #     pass
        #         # elif houre >= 1.3 and houre < 15:
        #         #     pass
        #             else:
        #                 print("====================")
        #                 print("out of schedule time")
        #                 print("====================")
        #
        #
        #
        # print("Final test ---------------")

    for id in StudentTD:
        x = CS1.objects.get(student_id=id)
        # weeks = [x.week_1, x.week_2,x.week_3,x.week_4,x.week_5,x.week_6,x.week_7]
        # global w
        # for w in weeks:
        #
        #     if w == '-1':
        #         if id in studentsIdWhoAttend:
        #             w = '1'
        #         else:
        #             w = '0'

        if x.week_1 == '-1':
            if id in studentsIdWhoAttend:
                x.week_1 = '1'
            else:
                x.week_1 = '0'
        elif x.week_2 == '-1':
            if id in studentsIdWhoAttend:
                x.week_2 = '1'
            else:
                x.week_2 = '0'
        elif x.week_3 == '-1':
            if id in studentsIdWhoAttend:
                x.week_3 = '1'
            else:
                x.week_3 = '0'
        elif x.week_4 == '-1':
            if id in studentsIdWhoAttend:
                x.week_4 = '1'
            else:
                x.week_4 = '0'
        elif x.week_5 == '-1':
            if id in studentsIdWhoAttend:
                x.week_5 = '1'
            else:
                x.week_5 = '0'
        elif x.week_6 == '-1':
            if id in studentsIdWhoAttend:
                x.week_6 = '1'
            else:
                x.week_6 = '0'
        elif x.week_7 == '-1':
            if id in studentsIdWhoAttend:
                x.week_7 = '1'
            else:
                x.week_7 = '0'
        
        x.save()
        # used to reset the RPi image table
        Image.objects.all().delete()



