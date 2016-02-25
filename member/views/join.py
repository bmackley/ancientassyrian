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

def process_request(request):	
	userLoggedIn = False
	if not request.user.is_authenticated():
		userLoggedIn = True
	else:	
		group = m.Group.objects.get(id=request.urlparams[0])
		members = m.Membership.objects.filter(group = group)
		for q in members:
			if q.member == request.user:
				return HttpResponseRedirect('/')
		user = request.user
		newMember = m.Membership()
		newMember.group = group
		newMember.member = user
		print(newMember.group)
		print(newMember.member)
		newMember.save()

	print(userLoggedIn)

	tvars={
		'userLoggedIn': userLoggedIn,
	}
	
	return templater.render_to_response(request, 'join.html', tvars)
	
