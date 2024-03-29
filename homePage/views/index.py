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
    if request.urlparams[0] == "logout":
        logout(request)
        return HttpResponseRedirect('/')
    if request.user.is_authenticated():
        return HttpResponseRedirect('/homePage/hotspots')
    form = LoginForm()
    createForm = CreateUserForm()
    if request.urlparams[0] == "1":
        createForm = CreateUserForm(request.POST)
        if createForm.is_valid():
            newUser = m.User()
            newUser.username = createForm.cleaned_data['username']
            newUser.email = createForm.cleaned_data['email']
            newUser.password = createForm.cleaned_data['password']
            newUser.save()
            return HttpResponseRedirect('/homePage/tutorial')
    else:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                userN = form.cleaned_data['username'].lower()
                user = authenticate(username = userN, password = form.cleaned_data['password'])
                if user is not None:
                    login(request, user)
                else:
                    raise forms.ValidationError("Please Enter a username") 
                return HttpResponseRedirect('/')
    if request.urlparams[0] == "about":
        tvars = {
            #'tablets': tablets,
            'form' : form,
            'createForm' : createForm,
        }
        return templater.render_to_response(request, 'about.html', tvars)
    if request.user.is_authenticated():
        identifiedChars = m.IdentifiedCharacter.objects.filter(user = request.user)
    else:
        identifiedChars = 'no characters'
    tvars = {
        #'tablets': tablets,
        'form' : form,
        'createForm' : createForm,
        'identifiedChars' : identifiedChars,
	}
    return templater.render_to_response(request, 'index.html', tvars)

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
class CreateUserForm(forms.Form):
    username = forms.CharField(required=True, label='Username', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(required=False, label='Email', widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(required=False, widget=forms.PasswordInput(attrs={'class':'form-control'}))  
    retypepassword = forms.CharField(required=False, label='Re-Enter Password',  widget=forms.PasswordInput(attrs={'class':'form-control'}))
    

    def __init__(self, *args, **kwargs):
            self.request = kwargs.pop('request', None)
            super(CreateUserForm, self).__init__(*args, **kwargs)

    def clean(self):
        if self.cleaned_data['username'] == "":
            raise forms.ValidationError("Please enter a username to sign up")
        if self.cleaned_data['password'] == "":
            raise forms.ValidationError("You must enter a password.")
        if self.cleaned_data['password'] != self.cleaned_data['retypepassword']:
            raise forms.ValidationError("The passwords do not match.")
        return self.cleaned_data




