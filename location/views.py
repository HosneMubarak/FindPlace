from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from .models import City, Country
from .serializers import CitySerializer, CountrySerializer


class CityListView(APIView):
    """
    list all city in the system.
    """

    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """
        Return a list of all city.
        """
        city_list = City.objects.all().order_by("city_name")
        serializer = CitySerializer(city_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CountryListView(APIView):
    """
    list all country in the system.
    """

    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """
        Return a list of all country.
        """
        city_list = Country.objects.all().order_by("name")
        serializer = CountrySerializer(city_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
