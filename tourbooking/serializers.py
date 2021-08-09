from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import * 

class TravelSerializer(ModelSerializer):
    class Meta:
        model = Travel
        fields = ["id","name","price","location","time","traffic"]


