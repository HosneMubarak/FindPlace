from django.urls import path
from .views import CityListView, CountryListView

urlpatterns = [
    path('city-list/', CityListView.as_view(), name='city-list'),
    path('country-list/', CountryListView.as_view(), name='country-list')
]
