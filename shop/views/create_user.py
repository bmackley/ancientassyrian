from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
#import of BOs
from Manager import models as m
from . import templater
import decimal, datetime
from django.contrib.auth import authenticate, login

def process_request(request):
	
		
	form = UsersForm(initial={
	'username':"",
	'email':"",
	'password':"",
	'retypepassword':"",
	'dateOfBirth':"",
	'gender':"",
	'weight':"",
	'height':"",

	})
	if request.method == 'POST':
		form = UsersForm(request.POST)
		if form.is_valid():
			users = m.User()
			users.username=form.cleaned_data[ 'username' ]
			users.email=form.cleaned_data[ 'email' ]
			users.set_password(form.cleaned_data['password'])
			users.dateOfBirth=form.cleaned_data['dateOfBirth']
			users.gender=form.cleaned_data['gender']
			users.weight=form.cleaned_data['weight']
			users.height=form.cleaned_data['height']
			users.save()
			
			return HttpResponseRedirect('/homePage/catalog/')	

	tvars={
	'form':form,
	}
	
	return templater.render_to_response(request, 'create_user.html', tvars)
	
class UsersForm(forms.Form):
	username = forms.CharField(required=True, label='Username', widget=forms.TextInput(attrs={'class':'form-control'}))
	email = forms.CharField(required=False, label='Email', widget=forms.TextInput(attrs={'class':'form-control'}))
	password = forms.CharField(required=False, widget=forms.PasswordInput(attrs={'class':'form-control'}))	
	retypepassword = forms.CharField(required=False, label='Re-Enter Password',  widget=forms.PasswordInput(attrs={'class':'form-control'}))
	dateOfBirth = forms.CharField(required=False, label='Birth Year', widget=forms.TextInput(attrs={'class':'form-control'}))
	gender = forms.ModelChoiceField(queryset=m.Gender.objects.all())
	weight = forms.CharField(required=False, label='Weight', widget=forms.TextInput(attrs={'class':'form-control'}))
	height = forms.CharField(required=False, label='Height', widget=forms.TextInput(attrs={'class':'form-control'}))

	def __init__(self, *args, **kwargs):
			self.request = kwargs.pop('request', None)
			super(UsersForm, self).__init__(*args, **kwargs)

	def clean(self):
			allUsers = m.User.objects.all()
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