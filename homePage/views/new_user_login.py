from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login
from homePage import models as m 
from . import templater

def process_request(request):
  print(request.urlparams[1])
  

  return templater.render_to_response(request, 'tutorial.html', tvars)
