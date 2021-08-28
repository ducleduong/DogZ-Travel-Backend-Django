from django.db import router
from django.urls import path
from django.urls.conf import include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('tours',views.ToursViewSet)
router.register('news',views.NewsViewSet)
router.register('comment',views.CommentViewSet)
router.register('rating',views.RatingViewSet)
router.register('review', views.ReviewTourViewSet)
router.register('like',views.LikeViewSet)
router.register('user',views.UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.index),
    path('api/all-like/<int:id>/' ,views.LikeViewSet.showListLikeOfNews),
    path('api/all-comment/<int:id>/', views.CommentViewSet.showListCommentOfNews),
    path('api/all-rating/<int:id>/',views.RatingViewSet.showListRatingOfTour),
    path('api/all-review/<int:id>/', views.ReviewTourViewSet.showListReviewOfNews)
]