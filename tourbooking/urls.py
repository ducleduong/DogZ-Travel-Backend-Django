from django.db import router
from django.urls import path
from django.urls.conf import include
from rest_framework import viewsets
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tours',views.ToursViewSet)
router.register('news',views.ListNewsViewSet)
router.register('comment',views.CommentViewSet)
router.register('like',views.LikeViewSet)
router.register('tourdetail',views.ToursDetailViewSet)
router.register('category',views.CategoryTourViewSet)
router.register('location',views.LocationViewSet)
router.register('rating',views.RatingViewSet)
router.register('user',views.UserViewSet)
router.register('order',views.RegisterTourViewSet)
router.register('register',views.RegisterUserViewSet)
router.register('newsdetail',views.NewsDetailViewSet)

urlpatterns = [
    path(r'api/', include(router.urls)),
    path(r'api/changepassword/', views.ChangePasswordView.as_view()),
    path(r'api/statistical/', views.getSum),
]