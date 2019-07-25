from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework.validators import UniqueValidator
from .models import Provider, ServiceArea


class ProviderSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    email = serializers.EmailField(validators=[UniqueValidator(queryset=Provider.objects.all())])
    phone = serializers.CharField()
    language = serializers.CharField()
    currency = serializers.CharField()

    def create(self, valid_data):
        provider = Provider(**valid_data)
        provider.save()
        return provider

    def update(self, instance, valid_data):
        instance.name = valid_data["name"]
        instance.email = valid_data["email"]
        instance.phone = valid_data["phone"]
        instance.language = valid_data["language"]
        instance.currency = valid_data["currency"]
        instance.save()
        return instance

    class Meta:
        model = Provider
        fields = '__all__'


class ServiceAreaSerializer(GeoFeatureModelSerializer):
    provider = ProviderSerializer(read_only=True)
    provider_id = serializers.PrimaryKeyRelatedField(source="provider", queryset=Provider.objects.all())

    class Meta:
        model = ServiceArea
        geo_field = 'polygon'
        fields = '__all__'

