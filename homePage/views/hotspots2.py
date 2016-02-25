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
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')
    if request.urlparams[0] == "logout":
        print('logout')
        logout(request)
        return HttpResponseRedirect('/')
    form = LoginForm()
    createForm = CreateUserForm()
    if request.urlparams[0] == "1":
        createForm = CreateUserForm(request.POST)
        if createForm.is_valid():
            newUser = m.User()
            print(createForm.cleaned_data['username'])
            newUser.username = createForm.cleaned_data['username']
            newUser.email = createForm.cleaned_data['email']
            newUser.password = createForm.cleaned_data['password']
            newUser.save()
            return HttpResponseRedirect('/')
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
    #for the main webpage
    tablets = m.Tablet.objects.get(name="VS 26 47")
    # for x in range(1,15):
    #     lines = m.Line()
    #     lines.tablet = tablets
    #     lines.side = "obv"
    #     lines.lineNumber = x
    #     lines.save()

    # newTablet = m.Tablet()
    # newTablet.name = 'VS 26 47'
    # newTablet.imagePath = '/static/homepage/images/VS_26_47.png'
    # newTablet.save()
    # newChar = m.MatchingCharacter()
    # newChar.filepath = "/static/homepage/images/8-01.png"
    # newChar.name = "8-01"
    # newChar.mimeType = "8-01"
    # newChar.save()
    #line = m.Line.objects.get(lineNumber = 1)
    characters = m.AssyrianChar.objects.filter(line = 2)
    sign = m.Sign.objects.all()[:20]
    #only get identified characters if user is logged in
    if request.user.is_authenticated():
        identifiedChars = m.IdentifiedCharacter.objects.filter(user = request.user)
        if not identifiedChars:
            identifiedChars = 'no characters'
        else:
            for i in identifiedChars:
                if i.sign is None:
                    print('None')
                else:
                    print(i.sign.filepath)
    else:
        identifiedChars = 'no characters'

    tvars = {
        'tablets': tablets,
        'sign' : sign,
        'form' : form,
        'createForm' : createForm,
        'identifiedChars' : identifiedChars,
        'characters' : characters,
	}
    return templater.render_to_response(request, 'hotspots.html', tvars)

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
        print('aaaaaa')
        print(self.cleaned_data['username'])
        print('bbbbbbb')
        if self.cleaned_data['username'] == "":
            raise forms.ValidationError("Please enter a username to sign up")
        if self.cleaned_data['username'] == m.User.objects.filter(username = self.cleaned_data['username']):
            raise forms.ValidationError("The username is taken.")
        if self.cleaned_data['email'] == m.User.objects.filter(email = self.cleaned_data['email']):
            raise forms.ValidationError("The email is in use.")
        if self.cleaned_data['password'] == "":
            raise forms.ValidationError("You must enter a password.")
        if self.cleaned_data['password'] != self.cleaned_data['retypepassword']:
            raise forms.ValidationError("The passwords do not match.")
        return self.cleaned_data
