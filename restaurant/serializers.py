from rest_framework import serializers
from .models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    city = serializers.CharField(source='city.city_name')
    category = serializers.CharField(source='category.category_name')

    class Meta:
        model = Restaurant
        fields = '__all__'
