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
	#Deletes hotspots. 
	if request.user.is_authenticated():
		if request.urlparams[2] == 'new':
			deleted_character_database = m.IdentifiedCharacter.objects.get(hotspot_x = request.urlparams[1], hotspot_y = request.urlparams[0])
			deleted_character_id = deleted_character_database.id
			print(request.urlparams[1])
			print(request.urlparams[2])
		else:
			deleted_character_id = request.urlparams[0]
			deleted_character_database = m.IdentifiedCharacter.objects.get(id = deleted_character_id)
		if deleted_character_database.user == request.user:
			m.IdentifiedCharacter.objects.filter(id = deleted_character_id).delete()
		
	

	tvars = {
	 
	}
	return templater.render_to_response(request, 'index.html', tvars)




