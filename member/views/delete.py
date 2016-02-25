from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
#import of BOs
from Manager import models as m
from . import templater
import decimal, datetime


def process_request(request):
	
	users = m.User.objects.get(id=request.urlparams[0])
	users.active = False;

	tvars={
	
	}
	
	return templater.render_to_response(request, 'delete.html', tvars)