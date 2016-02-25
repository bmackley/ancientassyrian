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
		##tw = m.Run.objects.filter(user = requst.user).latest('runDate')
		tr = m.Run.objects.filter(user = request.user).latest('runDate')
	except:
		tr = 0
	try:
		if(datetime.datetime.utcnow().replace(tzinfo=utc)-datetime.timedelta(days=1)) < (tr.runDate):
			form = weightForm(initial={
			'tRun': tr.distance,
			})
		else:
			form = weightForm(initial={
			'tRun':"",
			})
	except:
		print('there is not any runs yet')
		form = runForm(initial={
			'tRun':"",
			})
	if request.method == 'POST':
		print('this should be posting')
		form = runForm(request.POST)
		if form.is_valid():
			r = m.Run()
			print(request.user)
			r.user = request.user
			r.runDate = datetime.datetime.utcnow().replace(tzinfo=utc)
			r.distance = form.cleaned_data['tRun']
			total = Decimal(r.distance)
			if tr > 0:
				try:
					r.totalDistance = Decimal(tr.totalDistance) + total
				except:
					r.totalDistance = total
			else:
				r.totalDistance = total
			r.save()
			return HttpResponseRedirect('/member/run')	
	
	try:
		runs = m.Run.objects.filter(user = request.user)
		print('User weight')
	except:
		print('not working')
		runs = 0
	tvars={
	'form':form,
	'runs': runs,
	'tr':tr,
	}
	
	return templater.render_to_response(request, 'run.html', tvars)


class runForm(forms.Form):
	tRun = forms.CharField(required=True, label="Today's Run", max_length=3, widget=forms.TextInput(attrs={'class':'form-control'}))
	
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

