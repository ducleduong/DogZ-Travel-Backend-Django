from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import * 


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
    class Meta:
        model = ReviewTour
        fields = '__all__'

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class RatingSerializer(ModelSerializer):
    class Meta:
        model = RatingTour
        fields = '__all__'

class LikeSerializer(ModelSerializer):
    class Meta:
        model = RatingTour
        fields = '__all__'





