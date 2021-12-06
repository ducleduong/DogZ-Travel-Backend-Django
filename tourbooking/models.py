from typing import Text
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.fields import DateTimeField, FloatField, IntegerField, TextField
from ckeditor.fields import RichTextField
from django.db.models.fields.related import ForeignKey
import math

from rest_framework.fields import CharField

from tour.settings import DATETIME_FORMAT


#User
class User(AbstractUser):
    email = models.CharField(null=False, unique=True, max_length=100)
    password = models.CharField(null=False, max_length=100)
    last_name = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=11, null=True)
    avatar = models.ImageField(upload_to='avatar/', default='avatar/avatar-anonymous.png', blank=True, max_length=500)

    def booking_history(self):
        return OrderTour.objects.filter(user=self).order_by('-date_add')

#------LOCATION---------
class Location(models.Model):
    name = models.CharField(null=False, max_length=100)

    def __str__(self):
        return self.name


#Category of Tour
class CategoryTour(models.Model):
    name = models.CharField(null=False, max_length=100)

    def __str__(self):
        return self.name

#BASE of SERVICE and Tour
class ModelBase(models.Model):
    class Meta:
        abstract = True
    
    name = models.CharField(null=False, max_length=100)
    status = models.BooleanField(null=False)
    hotline = models.CharField(max_length=10, null=True)
    content = RichTextField()
    date_add = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)
    image = models.ImageField(default=None, upload_to='images/%Y/%m')
    views = models.IntegerField(null=False)
    destination = models.ForeignKey(Location,on_delete=SET_NULL,null=True)
    price = FloatField(default=0)
    price_children = FloatField(default=0)

    def __str__(self):
        return self.name

#Tour
class Tours(ModelBase):
    time = models.CharField(max_length=100, null=True)
    traffic = models.CharField(max_length=100, null=True)
    category_tour = models.ForeignKey(CategoryTour,on_delete=SET_NULL, null=True)
    start_date = models.DateField()

    def avg_rating(self):
        ratings = RatingTour.objects.filter(tour=self)
        if len(ratings) > 0:
            sum = 0
            for rating in ratings:
                sum += rating.star
            return math.floor(sum/len(ratings))
        return 0

    def all_rating(self):
        return RatingTour.objects.filter(tour=self).order_by('-date_add')

    def all_image(self):
        return TourImages.objects.filter(tour=self)

#News
class News(models.Model):
    name = models.CharField(null=False, max_length=100)
    views = models.IntegerField(null=False)
    status = models.BooleanField(null=False)
    content = RichTextField()
    date_add = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)
    user = models.ForeignKey(User,on_delete=SET_NULL,null=True)
    image = models.ImageField(default=None, upload_to='images/%Y/%m')
    overview = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.name

    def no_of_comment(self):
        return Comment.objects.filter(news=self).count()

    def no_of_like(self):
        return Like.objects.filter(news=self).count()

    def all_comment(self):
        return Comment.objects.filter(news=self).order_by('-date_add')

    def all_like(self):
        return Like.objects.filter(news=self)

#REVIEW BASE
class BaseReview(models.Model):
    class Meta:
        abstract = True
    
    content = models.TextField(max_length=1000,null=True)
    user = models.ForeignKey(User,on_delete=SET_NULL,null=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

#Rating Tour
class RatingTour(models.Model):
    tour = models.ForeignKey(Tours,on_delete=SET_NULL,null=True)
    star = models.IntegerField(default=5)
    content = TextField(max_length=1000,null=False)
    user = models.ForeignKey(User,on_delete=CASCADE)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
   

#Comment News
class Comment(BaseReview):
    news = models.ForeignKey(News,on_delete=SET_NULL,null=True)

#Like News
class Like(models.Model):
    class Meta:
        unique_together = (("user","news"),)

    news = models.ForeignKey(News,on_delete=CASCADE)
    user = models.ForeignKey(User,on_delete=CASCADE)

#Tours Image 
class TourImages(models.Model):
    tour = models.ForeignKey(Tours,on_delete=SET_NULL,null=True)
    image = models.ImageField(upload_to='images/%Y/%m')

    def __str__(self):
        return self.tour.name

#OrderTour
class OrderTour(models.Model):
    tour = ForeignKey(Tours,on_delete=CASCADE)
    user = ForeignKey(User,on_delete=CASCADE)
    date_add = DateTimeField(auto_now_add=True)
    adult = IntegerField()
    children = IntegerField()
    total = FloatField()