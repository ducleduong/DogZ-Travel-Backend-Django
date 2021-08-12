from django.db import router
from django.urls import path
from django.urls.conf import include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('travel',views.TravelViewSet)
router.register('news',views.NewsViewSet)
router.register('comment',views.CommentViewSet)
router.register('rating',views.RatingViewSet)
router.register('review', views.ReviewTravelViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.index)
]