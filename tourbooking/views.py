from django.shortcuts import render
from rest_framework import generics, viewsets, request, permissions
from rest_framework.response import Response
from .models import *
from .serializers import *

def index(request):
    return render(request,'index.html')

class UserViewSet(viewsets.ViewSet, generics.CreateAPIView,generics.RetrieveAPIView,generics.UpdateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'retrieve':
            return [permissions.IsAuthenticated()]
        
        return [permissions.AllowAny()]


class ToursViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    queryset = Tours.objects.filter(status=True)
    serializer_class = ToursSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.filter(status=True)
    serializer_class = NewsSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]
        
        return [permissions.IsAuthenticated()]


class ReviewTourViewSet(viewsets.ModelViewSet):
    queryset = ReviewTour.objects.all()
    serializer_class = ReviewTourSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]
        
        return [permissions.IsAuthenticated()]


class RatingViewSet(viewsets.ModelViewSet):
    queryset = RatingTour.objects.all()
    serializer_class = RatingSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]
        
        return [permissions.IsAuthenticated()]


class LikeViewSet(viewsets.ViewSet, generics.RetrieveDestroyAPIView,generics.ListAPIView,generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    
    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]
        
        return [permissions.IsAuthenticated()]








