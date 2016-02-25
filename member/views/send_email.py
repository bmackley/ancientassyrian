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

def process_request(request):	
	form = addUser(initial={
		'userInvite':""
		})
	
	if request.method == 'POST':
		form = addUser(request.POST)
		if form.is_valid:
			toEmail = form.cleaned_data['userInvite']
			message = "Welcome to compfitition!"  " \r\nThank you!\r\n\r\nCompFITition"
			send_mail('Welcome to CompFITition!', message, 'ben@compFITition.com', [toEmail], fail_silently=False)
			print(message)
			return HttpResponseRedirect('/member/send_email/')

	tvars={
	'form': form,
	}
	
	return templater.render_to_response(request, 'send_email.html', tvars)
	
class addUser(forms.Form):
	userInvite = forms.CharField(required=True, label="Enter E-mail", widget=forms.TextInput(attrs={'class':'form-control'}))
		
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

