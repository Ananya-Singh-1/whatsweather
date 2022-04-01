from rest_framework import serializers
from django.contrib.auth import get_user_model

from weather.models import Description

class UserSerializer2(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"

class DescriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Description
        fields = ['id','weather_description','temperature','created_on']