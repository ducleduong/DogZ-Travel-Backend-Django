from django.http import request
from django.shortcuts import render
from rest_framework import generics, serializers, viewsets, request
from rest_framework.response import Response
from .models import *
from .serializers import *

def index(request):
    return render(request,'index.html')

class TravelViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    queryset = Travel.objects.filter(status=True)
    serializer_class = TravelSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.filter(status=True)
    serializer_class = NewsSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class ReviewTravelViewSet(viewsets.ModelViewSet):
    queryset = ReviewTravel.objects.all()
    serializer_class = ReviewTravelSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = RatingTravel.objects.all()
    serializer_class = RatingSerializer







