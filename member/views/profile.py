from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from Manager import models as m #giving models alias m so we don't have to type it every time.
from . import templater

def process_request(request):
	
	try:
		groups = m.Membership.objects.filter(member = request.user) # get all membership objects from models. (SQL code in django form)
	except:
		groups = False 
	try:
		runs = m.Run.objects.filter(user = request.user).order_by('-id')[:1] # get all membership objects from models. (SQL code in django form)
		#runs = m.Run.objects.all()
	except:
		runs = False 
	for i in runs:
		print(i.totalDistance)
		print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
	tvars = {
		'groups' : groups,
		'runs' : runs,
	}
	return templater.render_to_response(request, 'profile.html', tvars)
	