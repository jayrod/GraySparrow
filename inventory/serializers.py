from django.contrib.auth.models import User, Group
from inventory.models import Location
from rest_framework import serializers


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ['description', ]