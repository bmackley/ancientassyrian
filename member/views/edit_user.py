from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
#import of BOs
from Manager import models as m
from . import templater
import decimal, datetime

Gender = (
         ('Male','Male'),
         ('Female','Female')
        )
def process_request(request):
	'''Edit a user'''
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/homePage/index')
		
	#print to console
	if request.urlparams[0] =='new':
		return HttpResponseRedirect('/shop/create_user/')
	else:
		users = m.User.objects.get(id=request.urlparams[0])
	print(users.height)
	try:
		ft = int(users.height/12)
	except:
		ft = 0
	print(ft)
	try: 
		form = UsersForm(initial={
			'username':users.username,
			'first_name':users.first_name,
			'last_name':users.last_name,
			'email':users.email,
			'zipcode':users.zipcode,
			'dateOfBirth': users.dateOfBirth,
			'gender': users.gender,
			'weight':users.weight,
			'feet': ft,
			'inches':users.height%12,
			
		})
	except:
		form = UsersForm(initial={
			'username':users.username,
			'first_name':users.first_name,
			'last_name':users.last_name,
			'email':users.email,
			'zipcode':users.zipcode,
			'dateOfBirth': users.dateOfBirth,
			'gender': users.gender,
			'weight':users.weight,
			'feet': ft,
			'inches':"",
			
		})
	if request.method == 'POST':
		form = UsersForm(request.POST)
		if form.is_valid():
			users.username=form.cleaned_data[ 'username' ]
			users.first_name=form.cleaned_data[ 'first_name' ]
			users.last_name=form.cleaned_data[ 'last_name' ]
			users.email=form.cleaned_data[ 'email' ]
			users.zipcode=form.cleaned_data['zipcode']
			users.dateOfBirth=form.cleaned_data['dateOfBirth']
			users.gender=form.cleaned_data['gender']
			users.weight=form.cleaned_data['weight']
			heightFT = form.cleaned_data['feet']
			heightIN = form.cleaned_data['inches']
			users.height=(int(heightFT)*12)+ int(heightIN)
			users.save()
			return HttpResponseRedirect('/member/index/') #change this after getting the homepage done
	
	tvars={
	'form':form,
	}
	
	return templater.render_to_response(request, 'edit_user.html', tvars)
	
class UsersForm(forms.Form):
	username = forms.CharField(required=True, label='Username', widget=forms.TextInput(attrs={'class':'form-control'}))
	first_name = forms.CharField(required=False, label='First Name', widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(required=False, label='Last Name', widget=forms.TextInput(attrs={'class':'form-control'}))
	email = forms.CharField(required=False, label='Email', widget=forms.TextInput(attrs={'class':'form-control'}))
	#address = forms.CharField(required=False, label='Address', widget=forms.TextInput(attrs={'class':'form-control'}))
	#city = forms.CharField(required=False, label='City', widget=forms.TextInput(attrs={'class':'form-control'}))
	#state = forms.CharField(required=False, label='State', widget=forms.TextInput(attrs={'class':'form-control'}))
	zipcode = forms.CharField(required=False, label='Zip Code', max_length=5, widget=forms.TextInput(attrs={'class':'form-control'}))
	#phone = forms.CharField(required=False, label='Phone', widget=forms.TextInput(attrs={'class':'form-control'}))
	dateOfBirth = forms.DateField(required=False, label='Birth Date', widget=forms.TextInput(attrs={'class':'form-control'}))
	gender = forms.TypedChoiceField(choices= Gender, initial='Male')
	weight = forms.ChoiceField(choices=[(x,x) for x in range(75,500)])
	feet = forms.ChoiceField(label='Height (ft)', choices=[(x,x) for x in range(2,8)])
	inches = forms.ChoiceField(label='Height (in)', choices=[(x,x) for x in range(0,12)])