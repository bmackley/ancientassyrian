from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login
from Manager import models as m 
from . import templater

def process_request(request):
  '''Shows the List of Stores'''
  
  form = LoginForm()
  if request.method == 'POST':

    form = LoginForm(request.POST)
    if form.is_valid():
      user = authenticate(lusername = form.cleaned_data['username'].lower(), password = form.cleaned_data['password'])
      if user is not None:
        if not request.user.is_superuser:
          login(request, user)
          redirect = request.META.get('HTTP_REFERER')
          return HttpResponse('<script>window.location.href="'+ redirect +'"</script>')
        else:
          login(request, user)
          return HttpResponse('<script>window.location.href="/Manager/stores/"</script>')
       
  tvars = {
  'form' : form,
  }

  return templater.render_to_response(request, 'base_template.html', tvars)

class LoginForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField(widget=forms.PasswordInput)

  def clean(self):
    user = authenticate(username = self.cleaned_data['username'], password = self.cleaned_data['password'])
    if user == None:
      raise forms.ValidationError("Incorrect password or Username") 
    return self.cleaned_data