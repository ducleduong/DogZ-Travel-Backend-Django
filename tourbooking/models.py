from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.fields import FloatField
from ckeditor.fields import RichTextField


#User
class User(AbstractUser):
    email = models.CharField(null=False, unique=True, max_length=100)
    status = models.BooleanField(default=1)
    password = models.CharField(null=False, max_length=100)
    last_name = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=100, null=True)

#------LOCATION---------
class Location(models.Model):
    name = models.CharField(null=False, max_length=100)

    def __str__(self):
        return self.name


#Category of Travel
class CategoryTravel(models.Model):
    name = models.CharField(null=False, max_length=100)

    def __str__(self):
        return self.name

#BASE of SERVICE and TRAVEL
class ModelBase(models.Model):
    class Meta:
        abstract = True
    
    name = models.CharField(null=False, max_length=100)
    status = models.BooleanField(null=False)
    hotline = models.CharField(max_length=10, null=True)
    content = RichTextField()
    date_add = models.TimeField(auto_now_add=True)
    date_update = models.TimeField(auto_now=True)
    image = models.ImageField(default=None, upload_to='images/%Y/%m')
    address = models.CharField(max_length=100,null=True)
    views = models.IntegerField(null=False)
    location = models.ForeignKey(Location,on_delete=SET_NULL,null=True)
    detail_location = models.CharField(max_length=200, null=True)
    price = FloatField(default=0)

    def __str__(self):
        return self.name

#Travel
class Travel(ModelBase):
    time = models.CharField(max_length=100, null=True)
    traffic = models.CharField(max_length=100, null=True)
    category_travel = models.ForeignKey(CategoryTravel,on_delete=SET_NULL, null=True)

#News
class News(models.Model):
    name = models.CharField(null=False, max_length=100)
    views = models.IntegerField(null=False)
    status = models.BooleanField(null=False)
    content = RichTextField()
    date_add = models.TimeField(auto_now_add=True)
    date_update = models.TimeField(auto_now=True)
    user = models.ForeignKey(User,on_delete=SET_NULL,null=True)
    image = models.ImageField(default=None, upload_to='images/%Y/%m')
    
    def __str__(self):
        return self.name

#REVIEW BASE
class BaseReview(models.Model):
    class Meta:
        abstract = True
    
    content = models.TextField(max_length=1000,null=True)
    user = models.ForeignKey(User,on_delete=SET_NULL,null=True)
    date_add = models.TimeField(auto_now_add=True)
    date_update = models.TimeField(auto_now=True)

    def __str__(self):
        return self.name

#Review Travel
class ReviewTravel(BaseReview):
    travel = models.ForeignKey(Travel,on_delete=SET_NULL,null=True)

#Rating Travel
class RatingTravel(models.Model):
    travel = models.ForeignKey(Travel,on_delete=SET_NULL,null=True)
    star = models.IntegerField(default=5)
    user = models.OneToOneField(User,on_delete=CASCADE,unique=True)
   

#Comment News
class Comment(BaseReview):
    news = models.ForeignKey(News,on_delete=SET_NULL,null=True)






