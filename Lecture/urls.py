from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import Subjectlist,SubjectAdd ,LecttureDetailsAdd,LecttureDetailslist, CS1List
#
# router = routers.DefaultRouter()
# router.register('fourth-subjects', SubjectDetailsView, basename='fourth-subjects')
# router.register('lecture', LectureView, basename='lecture')

urlpatterns = [
    path('subjectslist/', Subjectlist.as_view()),
    path('subjectsadd/', SubjectAdd.as_view()),
    # path('subjectsRet/<str:professor_name>/', SubjectRet.as_view()),
    path('lecturesdetailslist/', LecttureDetailslist.as_view()),
    path('lecturesdetailsadd/', LecttureDetailsAdd.as_view()),
    path('CS1list/', CS1List.as_view()),
]