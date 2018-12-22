from __future__ import unicode_literals
from .models import sensor_read, plant      #importing class from models
from django.shortcuts import render
from django.http import HttpResponse		#importing required libraries
import time
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login,logout
from django.views import generic
from django.views.generic import View
from .forms import UserForm
from .import control
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

@login_required(login_url='/sensor/')			#open only if you are logged in
def details(request,pid):						#receiving plantid to display its details
	p_max = len(plant.objects.all())
	last_plant = plant.objects.all()[p_max-1]
	if(int(pid) <= last_plant.plant_id):						#checking weather it is a valid id or not
		plant_obj = plant.objects.get(plant_id=pid)
		name = plant_obj.plant_name
		pl_id = plant_obj.plant_id
		n = len(plant_obj.sensor_read_set.all())
		if(n>=1):												#if sensor values exits take the latest values
			received_data = plant_obj.sensor_read_set.all()[len(plant_obj.sensor_read_set.all())-1]
			temp_data=str(received_data.tem_value)
			hum_data=str(received_data.hum_value)
			soil_data=str(received_data.soil_value)
			level_data=str(received_data.water_level)
			condition=str(received_data.condition)
		else:
			return HttpResponse('<h3><center>The number of values are not sufficient to display</center></h3>')

		al_tem=[]
		al_hum=[]
		al_soil=[]
		al_water=[]
		al_time=[]								#retreving last ten values from database to plot graph
		if(n >= 10):
			all_data = plant_obj.sensor_read_set.all()[n-10:n]
			for i in range(0,9):
				al_tem.append(float(all_data[i].tem_value))
				al_hum.append(float(all_data[i].hum_value))
				al_soil.append(float(all_data[i].soil_value))
				al_water.append(float(all_data[i].water_level))
				al_time.append(all_data[i].timeanddate)
		lis=[]
		for i in range(0,last_plant.plant_id+1):
			try:
				obj = plant.objects.get(plant_id=i)
			except plant.DoesNotExist:
				print "plant does not exists"
			else:
				lis.append(i)
		context={'al_time':al_time,'lis':lis,'pid':pl_id,'condition':condition,'name':name,'tem':temp_data,'hum':hum_data,'soil':soil_data,'level':level_data,'al_water':al_water,'al_soil':al_soil,'al_hum':al_hum,'al_tem':al_tem}
		return render(request,'sensor/index.html',context)
	else:
		return HttpResponse("<h3><center> The plant with plant id " +  pid +  " does not exists</center></h3>")

@login_required(login_url='/sensor/')			#open only if you are logged in
def index(request):
	plant_obj = plant.objects.get(plant_id=0)
	name = plant_obj.plant_name
	pl_id = plant_obj.plant_id
	p_max = len(plant.objects.all())
        last_plant = plant.objects.all()[p_max-1]
	received_data = plant_obj.sensor_read_set.all()[len(plant_obj.sensor_read_set.all())-1]
	n = len(plant_obj.sensor_read_set.all())
	all_data = plant_obj.sensor_read_set.all()[n-10:n]			#retrieve last ten values from database
	al_tem=[]
	al_hum=[]
	al_soil=[]
	al_water=[]
	al_time=[]
	for i in range(0,9):										#storing the last ten values to plot a graph
		al_tem.append(float(all_data[i].tem_value))
		al_hum.append(float(all_data[i].hum_value))
		al_soil.append(float(all_data[i].soil_value))
		al_water.append(float(all_data[i].water_level))
		
		al_time.append(all_data[i].timeanddate)
	#storing the last value to display them in dashboard
	temp_data=str(received_data.tem_value)
	hum_data=str(received_data.hum_value)
	soil_data=str(received_data.soil_value)
	level_data=str(received_data.water_level)
	condition=str(received_data.condition)
	
	lis=[]
	for i in range(0,last_plant.plant_id+1):
		try:
			obj = plant.objects.get(plant_id=i)
		except plant.DoesNotExist:
			print "plant does not exists"
		else:
			lis.append(i)
	#context is a dictionary which contains data that is displayed on dashboard 
	context={'al_time':al_time,'lis':lis,'pid':pl_id,'condition':condition,'name':name,'tem':temp_data,'hum':hum_data,'soil':soil_data,'level':level_data,'al_water':al_water,'al_soil':al_soil,'al_hum':al_hum,'al_tem':al_tem}
	return render(request,'sensor/index.html',context)


def getdata(request):
	if request.method=='GET' :					#receiving data from raspberry using GET method
		plant_id=request.GET['pid']
		tem_value=request.GET['temperature']
		hum_value=request.GET['humidity']
		soil_value=request.GET['soilmoisture']
		water_level=request.GET['waterlevel']
		watersensor=request.GET['watersensor']
		condition=request.GET['condition']
		sensor_obj=sensor_read()				#creating a new object and storing the received values and saving it to database
		plant_obj=plant.objects.get(plant_id=plant_id)
		plant_obj.sensor_read_set.create(condition=condition,tem_value=tem_value,hum_value=hum_value,soil_value=soil_value,water_level=water_level,watersensor=watersensor,timeanddate=time.asctime( time.localtime(time.time())))
		return HttpResponse("data saved in db")
	else:
		return HttpResponse("error")


@login_required(login_url='/sensor/')
def map(request):
	temp_data=[]				#empty list to store latest sensor values of all plants
	hum_data=[]
	soil_data=[]
	level_data=[]
	water_data=[]
	latitude=[]
	longitude=[]
	names=[]
	lis=[]
	p_max = len(plant.objects.all())	#no of plants
	last_plant = plant.objects.all()[p_max-1]
	for i in range(0,last_plant.plant_id+1):
		try:
			plant_obj = plant.objects.get(plant_id=i)	
		except plant.DoesNotExist:
			print "plant does not exists"
			lis.append(-1)
			temp_data.append(0)
			hum_data.append(0)
			soil_data.append(0)
			level_data.append(0)
			water_data.append(0)
			latitude.append(0)
			longitude.append(0)
		else:	
			plant_obj = plant.objects.get(plant_id=i)						#retrieving objects of plant i
			if(len(plant_obj.sensor_read_set.all()) >= 1):
				received_data = plant_obj.sensor_read_set.all()[len(plant_obj.sensor_read_set.all())-1]
				temp_data.append(float(received_data.tem_value))
				hum_data.append(float(received_data.hum_value))
				soil_data.append(float(received_data.soil_value))			#storing latest sensor values
				level_data.append(float(received_data.water_level))
				water_data.append(float(received_data.watersensor))
			latitude.append(float(plant_obj.latitude))
			longitude.append(float(plant_obj.longitude))
			lis.append(plant_obj.plant_id)
			names.append(plant_obj.plant_name)
	#sending this data to map.html
	context={'lis':lis,'names':names,'tem':temp_data,'hum':hum_data,'soil':soil_data,'level':level_data,'water':water_data,'no_of_plants':len(lis),'latitude':latitude,'longitude':longitude}
	return render(request,'sensor/map.html',context)
 

@login_required(login_url='/sensor/')		
def addplant(request):
	if request.method == 'POST':						  #receiving data using POST method
		longitude = request.POST.get('longitude', False)  #receiving latitude,longitude and plant name
		plantname = request.POST['plantname']
		latitude = request.POST['latitude']
		lati = float(latitude)
		longi = float(longitude)
		last_plant = plant.objects.all()[len(plant.objects.all())-1]				
		plant_obj = plant()								 #creating new plant object and assigning the received values
		plant_obj.plant_id = last_plant.plant_id + 1
		plant_obj.plant_name = plantname			
		plant_obj.latitude = lati
		plant_obj.longitude = longi
		plant_obj.save()
		#print plantname
		return redirect('/index')			#redirecting to home page after saving the plant
	return render(request, 'sensor/addplant.html')

@login_required(login_url='/sensor/')
def deleteplant(request):
	if request.method == 'POST':						  #receiving data using POST method
		plantid = request.POST.get('plantid', False)
		plantid = int(plantid)
		last_plant = plant.objects.all()[len(plant.objects.all())-1]
		if plantid <= last_plant.plant_id:
			required_plant = plant.objects.get(plant_id=plantid)
			required_plant.delete()
			return redirect('/index')
	return render(request, 'sensor/deleteplant.html')

@login_required(login_url='/sensor/')
def controlcenter(request):
	if request.method == 'POST':
		message = request.POST.get('message', False)
		status = 0
		if(request.POST.get('start',True) == True):
			status = 1
		if(request.POST.get('stop',True) == True):
			status = 0
		plantid = request.POST.get('drop',False)
		control.senddetails(str(message),str(status),str(plantid))
		return redirect('/index/controlcenter')
	p_max = len(plant.objects.all())
	lis=[]
	for i in range(0,p_max):
		try:
			obj = plant.objects.get(plant_id=i)
		except plant.DoesNotExist:
			print "plant does not exists"
		else:
			lis.append(i)
	context={'lis':lis}
	return render(request, 'sensor/ccenter.html',context)



class UserFormView(View):
	form_class = UserForm
	template_name = 'sensor/registration.html'
	#display blank form
	def get(self,request):
		form = self.form_class(None)		#initially form is empty
		return render(request,self.template_name,{'form':form})
		
	# process form data
	def post(self,request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit=False)
			#cleaned (normalized) data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()
											
			#returns User objects if credentials are correct
			user = authenticate(username=username,password=password)

			if user is not None:
				if user.is_active:
					login(request,user)
					return redirect('index')
		else:
			return render(request,self.template_name,{'status':"A user with that username already exists"})

def signin(request):
	
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				flag=1
				return redirect('/index')
			else:
				return render(request, 'sensor/registration.html', {'status': 'Your account has been disabled'})
		else:
			return render(request, 'sensor/registration.html', {'status': 'Invalid credentials'})
	return render(request, 'sensor/registration.html')	

def logout_view(request):
	logout(request)
	return redirect('/sensor/')