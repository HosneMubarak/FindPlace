from django.db import models
from category.models import Category
from location.models import City
# Create your models here.

class Restaurant(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='place_category')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='palace_city')
    place_name = models.CharField(max_length=200)
    address = models.CharField(max_length=255)
    rating = models.PositiveIntegerField(default=0)
    timing = models.CharField(max_length=200)
    phone = models.CharField(max_length=200, blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    instagram = models.URLField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    copon_cude = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.place_name
