from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login
from homePage import models as m 
from . import templater

def process_request(request):
  if request.method == 'POST':
    form = ForgotPassForm(request.POST)
  else:
    form = ForgotPassForm()    
  tvars = {
    'form' : form,
  }

  return templater.render_to_response(request, 'forgot_password.html', tvars)

class ForgotPassForm(forms.Form):
  email = forms.CharField(required=False, label='Email', widget=forms.TextInput(attrs={'class':'form-control'}))

  def clean(self):
    email = self.cleaned_data['email'].lower()
    return self.cleaned_data