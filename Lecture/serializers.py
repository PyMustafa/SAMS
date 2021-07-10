from rest_framework import serializers
from .models import LectureSchedule,Fourth_Year_Subjects, CS1


class Subjectserializer(serializers.ModelSerializer):
    class Meta:
        model = Fourth_Year_Subjects
        fields = '__all__'


class LectureDetailsserializer(serializers.ModelSerializer):
    class Meta:
        model = LectureSchedule
        fields = '__all__'


class CS1Serializer(serializers.ModelSerializer):
    class Meta:
        model = CS1
        fields = '__all__'