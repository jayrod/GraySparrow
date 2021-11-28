from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import permissions
from inventory.serializers import  LocationSerializer
from inventory.models import Location

def index(request):
    return HttpResponse("Hello, world. You're at the inventory index.") 


class LocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Locations to be viewed or edited.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer