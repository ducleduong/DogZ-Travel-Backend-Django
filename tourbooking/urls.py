from django.db import router
from django.urls import path
from django.urls.conf import include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('travel',views.TravelViewSet)
router.register('hotel',views.HotelViewSet)
router.register('news',views.NewsViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.index)
]