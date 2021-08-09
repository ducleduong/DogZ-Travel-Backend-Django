from django.db import router
from django.urls import path
from django.urls.conf import include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api/travel',views.TravelViewSet)

urlpatterns = [
    path('', include(router.urls))
]