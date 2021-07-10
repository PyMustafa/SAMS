from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import ImageCreate, ImageList, ImageView, FlagCreat, FlagList

router = routers.DefaultRouter()
# router.register('rass_image', ImageView, basename='rass_image')


urlpatterns = [
    # path('', include(router.urls)),
    path('image_create', ImageCreate.as_view()),
    path('image_list', ImageList.as_view()),

    path('flag_create', FlagCreat.as_view()),
    path('flag_list', FlagList.as_view()),
]