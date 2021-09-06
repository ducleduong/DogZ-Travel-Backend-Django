from django.http.response import JsonResponse
from rest_framework.serializers import ModelSerializer
from .models import * 
from rest_framework.response import Response
from rest_framework import status


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','last_name','first_name','username','email','password']
        extra_kwargs = {
            'password': {'write_only':'true'}
        }
    
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        return user

#Location
class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

#Tour
class CategoryTourSerializer(ModelSerializer):
    class Meta:
        model = CategoryTour
        fields = '__all__'

class ToursSerializer(ModelSerializer):
    category_tour = CategoryTourSerializer()
    destination = LocationSerializer()
    class Meta:
        model = Tours
        fields = '__all__'


#News
class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

#Review
class ReviewTourSerializer(ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = ReviewTour
        fields = '__all__'

class CommentSerializer(ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Comment
        fields = '__all__'

class RatingSerializer(ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = RatingTour
        fields = '__all__'

class LikeSerializer(ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = RatingTour
        fields = '__all__'





