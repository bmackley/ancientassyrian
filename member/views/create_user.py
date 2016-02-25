from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
#import of BOs
from Manager import models as m
from . import templater
import decimal, datetime
from django.contrib.auth import authenticate, login
from django import forms

Gender = (
         ('Male','Male'),
         ('Female','Female')
        )


def process_request(request):
	
		
	form = UsersForm(initial={
	'username':"",
	'email':"",
	'password':"",
	'retypepassword':"",
	'dateOfBirth':"",
	'gender':"",
	'weight':"",
	

	})
	if request.method == 'POST':
		form = UsersForm(request.POST)
		if form.is_valid():
			users = m.User()
			uname = form.cleaned_data[ 'username' ]
			users.username= uname.lower()
			users.lusername=users.username.lower()
			users.email=form.cleaned_data[ 'email' ]
			users.set_password(form.cleaned_data['password'])
			users.dateOfBirth=form.cleaned_data['dateOfBirth']
			users.gender=form.cleaned_data['gender']
			users.weight=form.cleaned_data['weight']
			users.feet=form.cleaned_data['feet']
			users.inches=form.cleaned_data['inches']
			users.height= (int(users.feet)*12+int(users.inches))
			users.save()
			message = "Welcome to compfitition!"  " \r\nThank you!\r\n\r\nCompFITition"
			send_mail('Welcome to CompFITition!', message, 'ben@compFITition.com', [users.email], fail_silently=False)
			return HttpResponseRedirect('/member/welcome/')	

	tvars={
	'form':form,
	}
	
	return templater.render_to_response(request, 'create_user.html', tvars)


class UsersForm(forms.Form):
	username = forms.CharField(required=True, label='Username', widget=forms.TextInput(attrs={'class':'form-control'}))
	email = forms.CharField(required=False, label='Email', widget=forms.TextInput(attrs={'class':'form-control'}))
	password = forms.CharField(required=False, widget=forms.PasswordInput(attrs={'class':'form-control'}))	
	retypepassword = forms.CharField(required=False, label='Re-Enter Password',  widget=forms.PasswordInput(attrs={'class':'form-control'}))
	dateOfBirth = forms.DateField(required=False, label='Date of Birth', widget=forms.TextInput(attrs={'class':'form-control'}))
	gender = forms.TypedChoiceField(choices= Gender, initial='Male')
	weight = forms.ChoiceField(choices=[(x,x) for x in range(75,500)], initial='100', label= 'Weight (lbs)')
	feet = forms.ChoiceField(required=True, label='Feet', choices=[(x,x) for x in range(3,8)], initial='5')
	inches = forms.ChoiceField(required=True, label='Inches', choices=[(x,x) for x in range(0,12)], initial='5')
	fields = (('feet', 'inches'))
	
	

	def __init__(self, *args, **kwargs):
			self.request = kwargs.pop('request', None)
			super(UsersForm, self).__init__(*args, **kwargs)

	def clean(self):
			allUsers = m.User.objects.all()
			for u in allUsers:
				if self.cleaned_data['username'] == '':
					raise forms.ValidationError("Please enter a username to sign up")
				if self.cleaned_data['username'] == u.username:
					raise forms.ValidationError("The username is taken.")
				if self.cleaned_data['email'] == u.email:
					raise forms.ValidationError("The email is in use.")
			if self.cleaned_data['password'] == "":
				raise forms.ValidationError("You must enter a password.")
			if self.cleaned_data['password'] != self.cleaned_data['retypepassword']:
				raise forms.ValidationError("The passwords do not match.")
			return self.cleaned_data