from __future__ import unicode_literals
from django.contrib import admin
from .models import sensor_read,plant

admin.site.register(sensor_read)		
admin.site.register(plant)