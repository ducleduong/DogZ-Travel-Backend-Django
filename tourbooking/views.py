from django.http import request
from django.shortcuts import render
from rest_framework import generics, serializers, viewsets, request
from rest_framework.response import Response
from .models import *
from .serializers import *

def index(request):
    return render(request,'index.html')

class ToursViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    queryset = Tours.objects.filter(status=True)
    serializer_class = ToursSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.filter(status=True)
    serializer_class = NewsSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class ReviewTourViewSet(viewsets.ModelViewSet):
    queryset = ReviewTour.objects.all()
    serializer_class = ReviewTourSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = RatingTour.objects.all()
    serializer_class = RatingSerializer

class LikeViewSet(viewsets.ViewSet, generics.RetrieveDestroyAPIView,generics.ListAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer







