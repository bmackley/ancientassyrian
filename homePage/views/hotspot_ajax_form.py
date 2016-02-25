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
	if not request.user.is_authenticated():
		return ('/')
	if request.urlparams[0] == 'new':
		idCharForm = m.IdentifiedCharacter()
		idCharForm.hotspot_x = request.urlparams[1]
		print(request.urlparams[2])
		idCharForm.hotspot_y = request.urlparams[2]
		print(request.urlparams[3])
		idCharForm.hotspot_height = request.urlparams[3]
		print(request.urlparams[4])
		idCharForm.hotspot_width = request.urlparams[4]
		print(request.urlparams[5])
		idCharForm.user = m.User.objects.get(username = request.urlparams[5])
		matchedSign = m.Sign.objects.get(id = request.urlparams[6])
		idCharForm.sign = matchedSign
		print(idCharForm.user)
		idCharForm.save()
		saved_idCharForm = m.IdentifiedCharacter.objects.get(hotspot_x = request.urlparams[1], hotspot_y = request.urlparams[2])

		hotspot_id = {
			"id" : saved_idCharForm.id
		}
		return JsonResponse(hotspot_id)
	if request.urlparams[0] == "update":
		print('update')
		idCharForm = m.IdentifiedCharacter.objects.get(id = request.urlparams[6])
		idCharForm.hotspot_x = request.urlparams[1]
		idCharForm.hotspot_y = request.urlparams[2]
		idCharForm.hotspot_height = request.urlparams[3]
		idCharForm.hotspot_width = request.urlparams[4]
		idCharForm.user = m.User.objects.get(username = request.urlparams[5])
		idCharForm.save()
	if request.urlparams[0] == "match":
		print(request.urlparams[1])
		print(request.urlparams[2])
		print(request.urlparams[3])

		idCharForm = m.IdentifiedCharacter.objects.get(hotspot_y = request.urlparams[1], hotspot_x = request.urlparams[2])
		print('working here')
		matchedSign = m.Sign.objects.get(id = request.urlparams[3])
		print('working here 2')
		idCharForm.sign = matchedSign

		idCharForm.save()
		print(idCharForm.id)
	tvars = {
	 
	}
	return templater.render_to_response(request, 'index.html', tvars)

class IdentifiedCharacter(forms.Form):
	user = forms.CharField(required=True, label='Username', widget=forms.TextInput(attrs={'class':'form-control'}))
	MatchingCharacter = forms.CharField(required=True, label='Username', widget=forms.TextInput(attrs={'class':'form-control'}))
	date_recorded = forms.DateField(initial=datetime.date.today)
	link = forms.CharField() 
	hotspot_x = forms.IntegerField()
	hotspot_height = forms.IntegerField()
	hotspot_y = forms.IntegerField()
	hotspot_width = forms.IntegerField()
	

	def __init__(self, *args, **kwargs):
			self.request = kwargs.pop('request', None)
			super(IdentifiedCharacter, self).__init__(*args, **kwargs)




