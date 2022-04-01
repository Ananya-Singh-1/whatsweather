from django.shortcuts import render
from django.db import models
from rest_framework import viewsets,serializers
from django.contrib.auth.models import User
from .serializers import UserSerializer2, DescriptionSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .models import Description

MIN_LENGTH = 8

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only = True, min_length = MIN_LENGTH, error_messages={"min_length": "Password must be longer than {MIN_LENGTH} characters."} )
    password2 = serializers.CharField(write_only = True, min_length = MIN_LENGTH, error_messages={"min_length": "Password must be longer than {MIN_LENGTH} characters."} )

    class Meta:
     model = User
     fields ="__all__"

 

    def validate(self, data):
        if data["password"]!= data ["password2"]:
            raise serializers.ValidationError("Password does not match.")
        return data

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name =validated_data["last_name"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user
    
    
class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer2

class UserViewSet2(viewsets.ModelViewSet):
    permission_classes =(IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()

class DescriptionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Description.objects.all()
    serializer_class = DescriptionSerializer