from django.db import models


# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='countrys')
    city_name = models.CharField(max_length=200)

    def __str__(self):
        return self.city_name
