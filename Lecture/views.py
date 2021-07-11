from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Fourth_Year_Subjects, LectureSchedule, CS1
from .serializers import Subjectserializer, LectureDetailsserializer, CS1Serializer
from SAMS.models import Student

# Create your views here.


class SubjectAdd(generics.CreateAPIView):
    queryset = Fourth_Year_Subjects.objects.all()
    serializer_class = Subjectserializer


class Subjectlist(generics.ListAPIView):
    queryset = Fourth_Year_Subjects.objects.all()
    serializer_class = Subjectserializer


#
# class SubjectRet(generics.RetrieveAPIView):
#     queryset = Fourth_Year_Subjects.objects.all()
#     serializer_class = Subjectserializer
#     lookup_field = 'professor_name'


class LecttureDetailsAdd(generics.CreateAPIView):
    queryset = LectureSchedule.objects.all()
    serializer_class = LectureDetailsserializer


class LecttureDetailslist(generics.ListAPIView):
    queryset = LectureSchedule.objects.all()
    serializer_class = LectureDetailsserializer
#
# class SubjectDetailsView(viewsets.ModelViewSet):
#     queryset = Fourth_Year_Subjects.objects.all()
#     serializer_class = Subjectserializer
#
#
# class LectureView(viewsets.ModelViewSet):
#     queryset = LectureSchedule.objects.all()
#     serializer_class = LectureDetailsserializer


class CS1List(generics.ListAPIView):
    queryset = CS1.objects.all()
    serializer_class = CS1Serializer
    # temp = Student.objects.values('Student_ID')
    # temp2 = CS1.objects.values('student_id')
    # for i in temp:
    #     for j in temp2:
    #         for k in temp:
    #             if j['student_id'] == i['Student_ID'] and k['Student_ID'] == i['Student_ID']:
    #                 var = CS1.objects.filter(student_id=j).delete()
    #                 b = CS1.objects.create(student_id=j)
    #                 CS1.student_id.add(b)
    #                 b.save()
    #                 CS1.save()
    #             else:
    #                var2 =CS1.objects.create(student_id=j)
    #                CS1.student_id.add(var2)
    #                CS1.save()
