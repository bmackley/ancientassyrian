from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from Manager import models as m 
from . import templater

def process_request(request):
	
	try:
		groups = m.Membership.objects.filter(member = request.user)
		for g in groups:
			print(g.group)
			print(g.group.groupName)
			print(g.group.administrator)
		for i in groups:
			print(i)
	except:
		groups = False
	
	tvars = {
	'groups' : groups,
	}
	return templater.render_to_response(request, 'userGroup.html', tvars)
	