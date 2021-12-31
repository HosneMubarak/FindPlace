from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from .models import Restaurant
from .serializers import RestaurantSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class RestaurantListView(generics.ListAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'city']
    search_fields = ['place_name']
    ordering_fields = ['rating']
