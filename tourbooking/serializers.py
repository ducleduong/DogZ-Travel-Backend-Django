from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import * 


#Location
class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

#Travel
class CategoryTravelSerializer(ModelSerializer):
    class Meta:
        model = CategoryTravel
        fields = '__all__'

class TravelSerializer(ModelSerializer):
    category_travel = CategoryTravelSerializer()
    location = LocationSerializer()
    class Meta:
        model = Travel
        fields = '__all__'


#News
class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

#Review
class ReviewTravelSerializer(ModelSerializer):
    class Meta:
        model = ReviewTravel
        fields = '__all__'

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class RatingSerializer(ModelSerializer):
    class Meta:
        model = RatingTravel
        fields = '__all__'



