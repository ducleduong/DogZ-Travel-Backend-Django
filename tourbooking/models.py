from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import SET_NULL
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

#-------SERVICE AND TRAVEL-----------
#Category Service
class CategoryHotel(models.Model):
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
    time_open = models.TimeField(null=False)
    time_close = models.TimeField(null=False)
    image = models.ImageField(default=None, upload_to='images/%Y/%m')
    address = models.CharField(max_length=100,null=True)
    views = models.IntegerField(null=False)
    location = models.ForeignKey(Location,on_delete=SET_NULL,null=True)
    time = models.CharField(max_length=100, null=True)
    traffic = models.CharField(max_length=100, null=True)
    price = FloatField(default=0)

    def __str__(self):
        return self.name

#Service
class Hotel(ModelBase):
    category_service = models.ForeignKey(CategoryHotel, on_delete=SET_NULL, null=True) 

#Travel
class Travel(ModelBase):
    category_travel = models.ForeignKey(CategoryTravel,on_delete=SET_NULL, null=True)

#News
class News(models.Model):
    name = models.CharField(null=False, max_length=100)
    views = models.IntegerField(null=False)
    status = models.BooleanField(null=False)
    content = models.TextField(max_length=1000,null=True)
    date_add = models.TimeField(auto_now_add=True)
    date_update = models.TimeField(auto_now=True)
    user = models.ForeignKey(User,on_delete=SET_NULL,null=True)
    image = models.ImageField(default=None, upload_to='images/%Y/%m')
    
    def __str__(self):
        return self.name


#IMAGES BASE
class ImagesBase(models.Model):
    class Meta:
        abstract = True
    
    image = models.ImageField(default=None, upload_to='images/%Y/%m')
    user = models.ForeignKey(User,on_delete=SET_NULL,null=True)
    date_add = models.TimeField(auto_now_add=True)
    date_update = models.TimeField(auto_now=True)

    def __str__(self):
        return self.name

#Images of Service
class ImagesHotel(ImagesBase):
    hotel = models.ForeignKey(Hotel,on_delete=SET_NULL,null=True)
   

#Images of Travel
class ImagesTravel(ImagesBase):
    travel = models.ForeignKey(Travel,on_delete=SET_NULL,null=True)

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
   

#Review Service
class ReviewHotel(BaseReview):
    hotel = models.ForeignKey(Hotel,on_delete=SET_NULL,null=True)

#Comment News
class Comment(BaseReview):
    news = models.ForeignKey(News,on_delete=SET_NULL,null=True)






