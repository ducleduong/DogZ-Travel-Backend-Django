from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import * 


#Location
class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class ProvincialSerializer(ModelSerializer):
    class Meta:
        model = Provincial
        fields = '__all__'

class DistrictSerializer(ModelSerializer):
    provincial = ProvincialSerializer()
    class Meta:
        model = District
        fields = '__all__'

class WardSerializer(ModelSerializer):
    district = DistrictSerializer()
    class Meta:
        model = Ward
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


#Hotel
class CategoryHotelSerializer(ModelSerializer):
    class Meta:
        model = CategoryHotel
        fields = '__all__'

class HotelSerializer(ModelSerializer):
    location = LocationSerializer()
    provincial = ProvincialSerializer()
    ward = WardSerializer()
    district = DistrictSerializer()
    class Meta:
        model = Hotel
        fields = '__all__'


#News
class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


#Images
class ImagesTravelSerializer(ModelSerializer):
    class Meta:
        model = ImagesTravel
        fields = '__all__'

class ImagesHotelSerializer(ModelSerializer):
    class Meta:
        model = ImagesHotel
        fields = '__all__'


#Review
class ReviewTravelSerializer(ModelSerializer):
    class Meta:
        model = ReviewTravel
        fields = '__all__'

class ReviewHotelSerializer(ModelSerializer):
    class Meta:
        model = ReviewHotel
        fields = '__all__'

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'



