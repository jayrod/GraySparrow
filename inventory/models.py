from django.db import models

class Location(models.Model):
    description = models.CharField(max_length=200)