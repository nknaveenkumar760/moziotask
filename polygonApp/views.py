from django.contrib.gis.geos import Point
from rest_framework.exceptions import APIException
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Provider, ServiceArea
from .serializers import ProviderSerializer, ServiceAreaSerializer
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import renderers, schemas


@api_view()
@renderer_classes([renderers.CoreJSONRenderer, ])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='Bookings API')
    return generator.get_schema()


# using django rest framework for the API
class ProviderView(ListCreateAPIView):
    """
       API endpoint that allows provider to be viewed or edited.

       create:
       Return a new instance of provider.

       list:
       Return all provider.
    """
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ProviderDetails(RetrieveUpdateDestroyAPIView):
    """
       API endpoint that allows Provider to be viewed or edited or deleted.

       retrieve:
       Return  provider instance.

       update:
       edit provider instance.

       destroy:
       delete provider instance
    """
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ServiceAreaView(ListCreateAPIView):
    """
       API endpoint that allows Service Area to be created or listed.

       create:
       Return a new instance of service_area.

       list:
       Return all service_area.
    """
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer


class ServiceAreaDetails(RetrieveUpdateDestroyAPIView):
    """
       API endpoint that allows Service Area to be viewed or edited or deleted.

       retrieve:
       Return  service_area instance.

       update:
       edit service_area instance.

       destroy:
       delete service_area instance
    """
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer


class ServiceAreaAPI(APIView):
    """
        Return a Service Area that Include the Point

    """
    def get(self, request, *args, **kwargs):
        params = request.query_params
        lat = params.get('lat', None)
        lng = params.get('lng', None)
        if lat and lng:
            try:
                lng = float(lng)
                lat = float(lat)
                pnt = Point(lng, lat)
            except (TypeError, ValueError):
                raise APIException('lat or lng format is invalid')
            service_areas = ServiceArea.objects.filter(polygon__intersects=pnt)
            serializer = ServiceAreaSerializer(service_areas, many=True)
            return Response(serializer.data)
        else:
            raise APIException('Both lat and lng parameters are required')

