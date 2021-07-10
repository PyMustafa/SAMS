from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Image, Flag
from .serializers import ImageSerializer, FlagSerializer

# Create your views here.


class FlagCreat(generics.CreateAPIView):
    queryset = Flag.objects.all()
    serializer_class = FlagSerializer


class FlagList(generics.ListAPIView):
    queryset = Flag.objects.all()
    serializer_class = FlagSerializer


class ImageCreate(generics.CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ImageView(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ImageList(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

#
# class FlagView(viewsets.ModelViewSet):
#     queryset = Flag.objects.all()
#     serializer_class = FlagSerializer