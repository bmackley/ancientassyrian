from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
#import of BOs
from Manager import models as m
from . import templater
import decimal, datetime


def process_request(request):
	'''Edit a single store'''
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/shop/login')

	
		
		
	#print to console
	if request.urlparams[0] =='new':
		return HttpResponseRedirect('/shop/create_user/')
	else:
		users = m.User.objects.get(id=request.urlparams[0])

	
	form = UsersForm(initial={
		'username':users.username,
		'first_name':users.first_name,
		'last_name':users.last_name,
		'email':users.email,
		'address':users.address,
		'city':users.city,
		'state':users.state,
		'zipcode':users.zipcode,
		'phone':users.phone,
		'dateOfBirth': users.dateOfBirth,
		'gender': users.gender,
		'weight':users.weight,
		'height':users.height,
		
	})
	if request.method == 'POST':
		form = UsersForm(request.POST)
		if form.is_valid():
			users.username=form.cleaned_data[ 'username' ]
			users.first_name=form.cleaned_data[ 'first_name' ]
			users.last_name=form.cleaned_data[ 'last_name' ]
			users.email=form.cleaned_data[ 'email' ]
			users.address=form.cleaned_data['address']
			users.city=form.cleaned_data['city']
			users.state=form.cleaned_data['state']
			users.zipcode=form.cleaned_data['zipcode']
			users.phone=form.cleaned_data['phone']
			users.dateOfBirth=form.cleaned_data['dateOfBirth']
			users.gender=form.cleaned_data['gender']
			users.weight=form.cleaned_data['weight']
			users.height=form.cleaned_data['height']
			users.save()
			return HttpResponseRedirect('/shop/index/') #change this after getting the homepage done
	
	tvars={
	'form':form,
	}
	
	return templater.render_to_response(request, 'edit_user.html', tvars)
	
class UsersForm(forms.Form):
	username = forms.CharField(required=True, label='Username', widget=forms.TextInput(attrs={'class':'form-control'}))
	first_name = forms.CharField(required=False, label='First Name', widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(required=False, label='Last Name', widget=forms.TextInput(attrs={'class':'form-control'}))
	email = forms.CharField(required=False, label='Email', widget=forms.TextInput(attrs={'class':'form-control'}))
	address = forms.CharField(required=False, label='Address', widget=forms.TextInput(attrs={'class':'form-control'}))
	city = forms.CharField(required=False, label='City', widget=forms.TextInput(attrs={'class':'form-control'}))
	state = forms.CharField(required=False, label='State', widget=forms.TextInput(attrs={'class':'form-control'}))
	zipcode = forms.CharField(required=False, label='Zip Code', widget=forms.TextInput(attrs={'class':'form-control'}))
	phone = forms.CharField(required=False, label='Phone', widget=forms.TextInput(attrs={'class':'form-control'}))
	dateOfBirth = forms.CharField(required=False, label='Birth_Year', widget=forms.TextInput(attrs={'class':'form-control'}))
	gender = forms.CharField(required=False, label='Gender', widget=forms.TextInput(attrs={'class':'form-control'}))
	weight = forms.CharField(required=False, label='Weight', widget=forms.TextInput(attrs={'class':'form-control'}))
	height = forms.CharField(required=False, label='Height', widget=forms.TextInput(attrs={'class':'form-control'}))
	