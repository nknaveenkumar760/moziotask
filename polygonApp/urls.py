from django.urls import path
from django.conf.urls import url


from . import views

urlpatterns = [
    path('v1/providers/', views.ProviderView.as_view(), name='providers'),
    path('v1/providers/<uuid:pk>/', views.ProviderDetails.as_view(), name='providers_details'),
    path('v1/service_areas/', views.ServiceAreaView.as_view(), name='service_areas_views'),
    path('v1/service_areas/<uuid:pk>/', views.ServiceAreaDetails.as_view(), name='service_areas_details'),
    path('v1/get_areas/', views.ServiceAreaAPI.as_view(), name='providers'),
    url('docs', views.schema_view, name="schema_view"),

]



