from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
#import of BOs
from Manager import models as m
from . import templater
import decimal, datetime


def process_request(request):
	
	users = m.User.objects.get(id=request.urlparams[0])

	
	form = UsersForm(initial={

		'password':users.password,
	})
	if request.method == 'POST':
		form = UsersForm(request.POST)
		if form.is_valid():
			users.set_password(form.cleaned_data['password'])
			users.save()
			return HttpResponseRedirect('/homePage/catalog/')
	
	tvars={
	'form':form,
	}
	
	return templater.render_to_response(request, 'create_user.html', tvars)
	
class UsersForm(forms.Form):
	password = forms.CharField(required=False, widget=forms.PasswordInput(attrs={'class':'form-control'}))	


	
