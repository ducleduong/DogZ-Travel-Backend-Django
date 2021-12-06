from django.contrib.auth.models import Group, GroupManager
from django.db.models import fields
from django.http.response import JsonResponse
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from .models import * 
from rest_framework.response import Response
from rest_framework import status

class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class CategoryTourSerializer(ModelSerializer):
    class Meta:
        model = CategoryTour
        fields = '__all__'


class ListToursSerializer(ModelSerializer):
    destination = LocationSerializer()
    category_tour = CategoryTourSerializer()
    ratings = serializers.IntegerField(source='avg_rating')

    class Meta:
        model = Tours
        fields = ['id','name','destination','time','traffic','image','price','start_date','ratings','category_tour','views']


class RegisterTourSerializer(ModelSerializer):
    class Meta:
        model = OrderTour
        fields = '__all__'


class OrderTourSerializer(ModelSerializer):
    date_add = serializers.DateTimeField(format=DATETIME_FORMAT, input_formats=None)
    tour = ListToursSerializer()
    class Meta:
        model = OrderTour
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Group
        fields = ('name',)


class UserSerializer(ModelSerializer):
    groups = GroupSerializer(many=True)
    booking_history = OrderTourSerializer(many=True)
    class Meta:
        model = User
        fields = ['id','last_name','first_name','username','email','password','address','phone_number','avatar','booking_history', 'groups']
        extra_kwargs = {
            'password': {'write_only':'true'}
        }
    
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        return user


class RegisterUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','last_name','first_name','username','email','password','avatar']
        extra_kwargs = {
            'password': {'write_only':'true'}
        }
    
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        return user


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class UserCommentSerializer(ModelSerializer):
    groups = GroupSerializer(many=True)
    class Meta:
        model = User
        fields = ['id','last_name','first_name','avatar','groups','username']


class RatingSerializer(ModelSerializer):
    user = UserCommentSerializer()
    date_add = serializers.DateTimeField(format=DATETIME_FORMAT, input_formats=None)
    class Meta:
        model = RatingTour
        fields = '__all__'


class TourImageSerializer(ModelSerializer):
    class Meta:
        model = TourImages
        fields = ['image']


class RatingPostSerializer(ModelSerializer):
    class Meta:
        model = RatingTour
        fields = '__all__'


#Tour
class ToursDetailSerializer(ModelSerializer):
    category_tour = CategoryTourSerializer()
    destination = LocationSerializer()
    ratings = serializers.IntegerField(source='avg_rating')
    all_rating = RatingSerializer(many=True)
    all_image = TourImageSerializer(many=True)
    class Meta:
        model = Tours
        fields = '__all__'


#News
class CommentSerializer(ModelSerializer):
    user = UserCommentSerializer()
    date_add = serializers.DateTimeField(format=DATETIME_FORMAT, input_formats=None)
    class Meta:
        model = Comment
        fields = '__all__'


class CommentPostSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class LikeSerializer(ModelSerializer):
    user = UserCommentSerializer()
    class Meta:
        model = Like
        fields = '__all__'


class LikePostSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class NewsSerializer(ModelSerializer):
    all_comment = CommentSerializer(many=True)
    all_like = LikeSerializer(many=True)
    user = UserCommentSerializer()
    
    class Meta:
        model = News
        fields = '__all__'


class RecentNewsSerializer(ModelSerializer):
    comment = serializers.IntegerField(source='no_of_comment')
    like = serializers.IntegerField(source='no_of_like')
    user = UserCommentSerializer()
    class Meta:
        model = News
        fields = ['id','name','views','date_add','image','overview','like','comment','user']









