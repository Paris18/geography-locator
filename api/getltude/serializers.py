#django/rest_framework imports.
from rest_framework import serializers

# app level imports
from .models import (
                    AdressLtude,       
                    )

# list longitude and latitude details serializer
class AddresLtudeGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdressLtude
        fields = "__all__"


# add latitude longitude data serializer
class AddresLtudeAddSerializer(serializers.ModelSerializer):
	
    class Meta:
        model = AdressLtude
        fields = "__all__"

    def create(self,validated_data):
    	return AdressLtude.objects.create(**validated_data)

