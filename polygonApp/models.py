import uuid
from django.contrib.gis.db import models
from django.conf.global_settings import LANGUAGES


# Create your models here.

class Provider(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField("Provider Name", max_length=255)
    email = models.EmailField("Provider Email", unique=True, max_length=255)
    currency = models.CharField("Provider Currency", max_length=10)
    language = models.CharField("Provider Language", max_length=40, choices=LANGUAGES, default='en')
    phone = models.CharField("Provider Phone Number", max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


class ServiceArea(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    provider = models.ForeignKey('Provider', on_delete=models.CASCADE, related_name='service_areas')
    name = models.CharField("Name", max_length=100)
    price = models.DecimalField("Price", max_digits=60, decimal_places=2)
    polygon = models.PolygonField("Polygon", geography=True)

    def __str__(self):
        return self.name

