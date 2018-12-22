from django.conf.urls import include,url
from . import views
urlpatterns = [
	url(r'^$', views.signin ,name = "signin"),							#directs to sign in page 
    url(r'^index/$', views.index ,name = "index"),						#directs to home page
    url(r'^index/(?P<pid>[0-999]+)/$', views.details, name="details"),	#directs to particular plant page
    url(r'^index/map/$', views.map,name ="get1"),						#directs to map
    url(r'^get/$', views.getdata ,name ="get"),							#particularly to get data form raspberry
   	url(r'^register/$', views.UserFormView.as_view() ,name = "register"),#directs to register page
   	url(r'^index/addplant/$', views.addplant ,name="addplant"),			#directs to addplant page
   	url(r'^index/logout/$', views.logout_view ,name="logout"),			#directs to login page after logging out
    url(r'^index/controlcenter/$', views.controlcenter ,name="controlcenter"),
    url(r'^index/deleteplant/$', views.deleteplant ,name="deleteplant"),			#directs to addplant page
]