from django.shortcuts import render
from rest_framework import generics, serializers, viewsets, request, permissions
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

    def showListCommentOfNews(request,id):
        if request.method == 'GET':
            list = Comment.objects.filter(news=id)
            serializer = CommentSerializer(list, many=True)
            return JsonResponse(serializer.data, safe=False)


class ReviewTourViewSet(viewsets.ModelViewSet):
    queryset = ReviewTour.objects.all()
    serializer_class = ReviewTourSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]
        
        return [permissions.IsAuthenticated()]

    def showListReviewOfNews(request,id):
        if request.method == 'GET':
            list = ReviewTour.objects.filter(tour=id)
            serializer = ReviewTourSerializer(list, many=True)
            return JsonResponse(serializer.data, safe=False)


class RatingViewSet(viewsets.ViewSet,generics.ListAPIView,generics.CreateAPIView):
    queryset = RatingTour.objects.all()
    serializer_class = RatingSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]
        
        return [permissions.IsAuthenticated()]

    def showListRatingOfTour(request,id):
        if request.method == 'GET':
            list = RatingTour.objects.filter(tour=id)
            serializer = RatingSerializer(list, many=True)
            return JsonResponse(serializer.data, safe=False)


class LikeViewSet(viewsets.ViewSet,generics.RetrieveDestroyAPIView,generics.ListAPIView,generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    
    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]
        
        return [permissions.IsAuthenticated()]

    def showListLikeOfNews(request,id):
        if request.method == 'GET':
            list = Like.objects.filter(news=id)
            serializer = LikeSerializer(list, many=True)
            return JsonResponse(serializer.data, safe=False)








