from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    items = models.TextField()
    lat_long = models.CharField(max_length=255)
    full_details = models.TextField()
