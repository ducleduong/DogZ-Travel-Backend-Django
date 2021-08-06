from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import SET_NULL

#User
class User(AbstractUser):
    email = models.CharField(null=False, unique=True, max_length=100)
    status = models.BooleanField()
    password = models.CharField(null=False, max_length=100)
    last_name = models.CharField(max_length=100, null=False)
    first_name = models.CharField(max_length=100, null=False)
    role = models.IntegerField(null=False)

#------LOCATION---------
#Provincial
class Provincial(models.Model):
    name = models.CharField(null=False, max_length=100)
    category = models.CharField(max_length=100)

#District
class District(models.Model):
    name = models.CharField(null=False, max_length=100)
    category = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    provincial = models.ForeignKey(Provincial, on_delete=SET_NULL, null=True)

#Ward
class Ward(models.Model):
    name = models.CharField(null=False, max_length=100)
    category = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=SET_NULL, null=True)


#-------SERVICE AND TRAVEL-----------
#Category Service
class CategoryService(models.Model):
    name = models.CharField(null=False, max_length=100)
    category_parent = models.BooleanField(null=False)

#Category of Travel
class CategoryTravel(models.Model):
    name = models.CharField(null=False, max_length=100)

#Service
class Service(models.Model):
    category_service = models.ForeignKey(CategoryService, on_delete=SET_NULL, null=True)
    name = models.CharField(null=False, max_length=100)
    status = models.BooleanField(null=False)
    hotline = models.CharField(max_length=10, null=True)
    content = models.TextField(max_length=1000,null=True)
    date_add = models.TimeField(auto_now_add=True)
    date_update = models.TimeField(auto_now=True)
    user = models.ForeignKey(User,on_delete=SET_NULL,null=True)
    time_open = models.TimeField(null=False)
    time_close = models.TimeField(null=False)
    ward = models.ForeignKey(Ward,on_delete=SET_NULL,null=True)
    image = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100,null=True)
    lat = models.CharField(max_length=100,null=True)
    lng = models.CharField(max_length=100,null=True)
    views = models.IntegerField(null=False)
    price_min = models.FloatField(null=True)
    price_max = models.FloatField(null=True)

#News
class News(models.Model):
    name = models.CharField(null=False, max_length=100)
    views = models.IntegerField(null=False)
    status = models.BooleanField(null=False)
    content = models.TextField(max_length=1000,null=True)
    date_add = models.TimeField(auto_now_add=True)
    date_update = models.TimeField(auto_now=True)
    user = models.ForeignKey(User,on_delete=SET_NULL,null=True)
    image = models.CharField(max_length=100,null=True)

#Travel
class Travel(models.Model):
    category_travel = models.ForeignKey(CategoryTravel,on_delete=SET_NULL, null=True)
    name = models.CharField(null=False, max_length=100)
    status = models.BooleanField(null=False)
    content = models.TextField(max_length=1000,null=True)
    time_open = models.TimeField(null=False)
    time_close = models.TimeField(null=False)
    date_add = models.TimeField(auto_now_add=True)
    date_update = models.TimeField(auto_now=True)
    user = models.ForeignKey(User,on_delete=SET_NULL,null=True)
    ward = models.ForeignKey(Ward,on_delete=SET_NULL,null=True)
    image = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100,null=True)
    hotline = models.CharField(max_length=10, null=True)
    lat = models.CharField(max_length=100,null=True)
    lng = models.CharField(max_length=100,null=True)
    views = models.IntegerField(null=False)

#Images of Service
class ImagesService(models.Model):
    image = models.CharField(max_length=100,null=True)
    user = models.ForeignKey(User,on_delete=SET_NULL,null=True)
    service = models.ForeignKey(Service,on_delete=SET_NULL,null=True)
    date_add = models.TimeField(auto_now_add=True)
    date_update = models.TimeField(auto_now=True)

#Images of Travel
class ImagesTravel(models.Model):
    image = models.CharField(max_length=100,null=True)
    user = models.ForeignKey(User,on_delete=SET_NULL,null=True)
    travel = models.ForeignKey(Travel,on_delete=SET_NULL,null=True)
    date_add = models.TimeField(auto_now_add=True)
    date_update = models.TimeField(auto_now=True)

#Review Travel
class ReviewTravel(models.Model):
    content = models.TextField(max_length=1000,null=True)
    user = models.ForeignKey(User,on_delete=SET_NULL,null=True)
    travel = models.ForeignKey(Travel,on_delete=SET_NULL,null=True)
    date_add = models.TimeField(auto_now_add=True)
    date_update = models.TimeField(auto_now=True)

#Review Service
class ReviewService(models.Model):
    content = models.TextField(max_length=1000,null=True)
    user = models.ForeignKey(User,on_delete=SET_NULL,null=True)
    service = models.ForeignKey(Service,on_delete=SET_NULL,null=True)
    date_add = models.TimeField(auto_now_add=True)
    date_update = models.TimeField(auto_now=True)

#Comment
class Comment(models.Model):
    content = models.TextField(max_length=1000,null=True)
    user = models.ForeignKey(User,on_delete=SET_NULL,null=True)
    news = models.ForeignKey(News,on_delete=SET_NULL,null=True)
    date_add = models.TimeField(auto_now_add=True)
    date_update = models.TimeField(auto_now=True)






