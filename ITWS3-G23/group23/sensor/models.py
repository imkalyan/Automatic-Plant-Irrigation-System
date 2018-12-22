from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class plant(models.Model):						#plant class with required attributes
	plant_id = models.IntegerField(default=0)
	plant_name = models.CharField(max_length=250,default="tulasi")
	latitude = models.CharField(max_length=250,default=13.5515)
	longitude = models.CharField(max_length=250,default=79.9954)
	def __str__(self):
		return ("plant " + str(self.plant_id))

class sensor_read(models.Model):				#sensor class with different sensors
	plant_id = models.ForeignKey(plant, on_delete=models.CASCADE, default=0)
	#plant_id = models.IntegerField()
	#plant_id = models.AutoField(primary_key=True)
	tem_value = models.CharField(max_length=250,default=0)
	hum_value = models.CharField(max_length=250,default=0)
	soil_value = models.CharField(max_length=250,default=0)
	water_level = models.CharField(max_length=250,default=0)
	watersensor = models.CharField(max_length=250,default=0)
	condition = models.CharField(max_length=250,default="no condition")
	timeanddate = models.CharField(max_length=250,default=0)