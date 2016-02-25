from django import forms
from django.conf import settings
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login
from django.conf import settings
import decimal, datetime
from homePage import models as m
from django.contrib.auth import logout
from . import templater
import datetime

def process_request(request):
	#Saves the hotspots that were created. 
	print(request.urlparams[0])
	print(request.urlparams[1])
	print(request.urlparams[2])
	print(request.urlparams[3])
	if(request.urlparams[0] == "username"):
		try:
			user = m.User.objects.get(username = request.urlparams[1])
			userdata = {
				"users" : user.id
			}
		except:
			userdata = {
				"users" : 'no users'
			}
		if(request.urlparams[2] == "email"):
			try:
				user = m.User.objects.get(email = request.urlparams[1])
				userdata["email"] = user.email
			except:
				userdata["email"] = "no email"
		return JsonResponse(userdata)
	tvars = {
	 
	}
	return templater.render_to_response(request, 'index.html', tvars)