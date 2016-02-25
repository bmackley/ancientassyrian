from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login
from homePage import models as m 
from django.contrib.auth import logout
from . import templater

def process_request(request):
	logout(request)
	return HttpResponseRedirect('/')
