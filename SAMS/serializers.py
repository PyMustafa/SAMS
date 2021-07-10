from rest_framework import serializers
from .models import *
from account.models import Account
from rest_auth.serializers import LoginSerializer as RestAuthLoginSerializer


# for disable the default username field
class LoginSerializer(RestAuthLoginSerializer):
    username = None


class AccountSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

    class Meta:
        model = Account
        fields = ('email', 'password', 'is_admin', 'is_superuser', 'is_staff')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'


# class YEARSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = YEAR
#         fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class FlagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flag
        fields = '__all__'