from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import *
from .serializers import *

class TravelViewSet(viewsets.ModelViewSet):
    queryset = Travel.objects.filter(status=True)
    serializer_class = TravelSerializer


