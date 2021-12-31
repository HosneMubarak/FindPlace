from django.urls import path
from .views import RestaurantListView

urlpatterns = [
    path('restaurant-list/', RestaurantListView.as_view(), name='restaurant-list'),
]
