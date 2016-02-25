from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login
from django.conf import settings
import decimal, datetime
from homePage import models as m
from django.contrib.auth import logout
from . import templater
import datetime

def process_request(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
	 
    tvars = {

	}
    return templater.render_to_response(request, 'tutorial3.html', tvars)
