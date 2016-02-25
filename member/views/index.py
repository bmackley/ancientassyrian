from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
#import of BOs
from Manager import models as m
from . import templater
import decimal, datetime
from django.utils.timezone import utc
from django.contrib.auth import authenticate, login
from django import forms
from decimal import *

def process_request(request):
	if not request.user.is_authenticated():
		HttpResponseRedirect('/')
	try:
		tw = m.Weight.objects.filter(user = requst.user).latest('dateWeighed')
	except:
		print('No weight entries yet')
	try:
		if(datetime.datetime.utcnow().replace(tzinfo=utc)-datetime.timedelta(days=1)) < (tw.dateWeighed): #do we want this to be time delta or just the following day at any time is allowed?
			print(tw)
			print(tw.dateWeighed)
			print(datetime.datetime.now())
			print(datetime.datetime.now()-datetime.timedelta(days=1))
			form = weightForm(initial={
			'tWeight': tw.weight,
			})
		else:
			form = weightForm(initial={
			'tWeight':"",
			})
	except:
		print('there are not any weight entries yet')
		form = weightForm(initial={
			'tWeight':"",
			})
	if request.method == 'POST':
		print('this should be posting')
		form = weightForm(request.POST)
		if form.is_valid():
			print('a')
			w = m.Weight()
			print('aaaaaaaaaaa')
			w.user = request.user
			print('b')
			w.dateWeighed = datetime.datetime.utcnow().replace(tzinfo=utc) #added .strftime("%Y") to end. Didn't do anything
			print(w.dateWeighed)
			w.weight = form.cleaned_data['tWeight']
			print(w.weight)
			convertedWeight = Decimal(w.weight)
			if not (request.user.weight):
				uweight = Decimal(0.0)
			else:
				uweight = request.user.weight
			w.weightLost = uweight - convertedWeight
			print(request.user.weight)
			print(w.weightLost)
			w.save()
			print('abcabcab')
			return HttpResponseRedirect('/member/index')	
	
	try:
		weights = m.Weight.objects.filter(user = request.user)
		print('User weight')
	except:
		weights = m.Weight.objects.all()
		for w in weights:
			print(w.weight)
	tvars={
	'form':form,
	'weights': weights,
	}
	
	return templater.render_to_response(request, 'index.html', tvars)


class weightForm(forms.Form):
	tWeight = forms.CharField(required=True, label="Today's Weigh in", max_length=3, widget=forms.TextInput(attrs={'class':'form-control'}))
	
'''
	def __init__(self, *args, **kwargs):
			self.request = kwargs.pop('request', None)
			super(weightForm, self).__init__(*args, **kwargs)

	def clean(self):
			weight = m.User.objects.all()
			for u in allUsers:
				if self.cleaned_data['username'] == u.username:
					raise forms.ValidationError("The username is taken.")
				if self.cleaned_data['email'] == u.email:
					raise forms.ValidationError("The email is in use.")
			if self.cleaned_data['password'] == "":
				raise forms.ValidationError("You must enter a password.")
			if self.cleaned_data['password'] != self.cleaned_data['retypepassword']:
				raise forms.ValidationError("The passwords do not match.")
			return self.cleaned_data
'''

