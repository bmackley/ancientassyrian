from django.core.mail import EmailMultiAlternatives

from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from Manager import models as m
from . import templater
from django.conf import settings
import decimal, datetime

def process_request(request):	
	
	tvars = {
		
	}
	return templater.render_to_response(request, 'welcome.html', tvars)
