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
	
	form = GroupForm(initial={
	'groupName': "",
	# Andrew M. Commented out phone because not requisit
	#'city': "",
	#'state': "",
	'zipcode': "",
	
	#'phone': "",
	})

	if request.method == 'POST': 
		form = GroupForm(request.POST)
		if form.is_valid():
			groupMember = m.Membership()
			groupMember.member = request.user
			groupMember.save()
			group = m.Group()
			group.administrator = request.user
			group.groupName = form.cleaned_data['groupName']
			group.lgroupName = group.groupName.lower()
			# Andrew M. Commented out phone because not requisit
			#group.city = form.cleaned_data['city']
			#group.state = form.cleaned_data['state']
			group.zipcode = form.cleaned_data['zipcode']
			# Andrew M. Commented out phone because not requisit
			#group.phone = form.cleaned_data['phone']
			group.save()
			groupMember.group = group
			groupMember.save()
			return HttpResponseRedirect('/Manager/groups/' + str(group.id ))
			 	

	tvars={
	'form':form,
	}
	
	return templater.render_to_response(request, 'create_group.html', tvars)
	
class GroupForm(forms.Form):
	groupName = forms.CharField(required=True, label='Group Name', widget=forms.TextInput(attrs={'class':'form-control'}))
	# Andrew M. Commented out phone because not requisit
	#city = forms.CharField(required=False, label='City', widget=forms.TextInput(attrs={'class':'form-control'}))
	#state = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
	zipcode = forms.CharField(required=False, label='Zip Code', widget=forms.TextInput(attrs={'class':'form-control'}))
	# Andrew M. Commented out phone because not requisit
	#phone = forms.CharField(required=False, label='Phone', widget=forms.TextInput(attrs={'class':'form-control'}))

	def __init__(self, *args, **kwargs):
			self.request = kwargs.pop('request', None)
			super(GroupForm, self).__init__(*args, **kwargs)

	def clean(self):
			allGroups = m.Group.objects.all()
			for u in allGroups:
				if self.cleaned_data['groupName'] == u.groupName:
					raise forms.ValidationError("The group name is taken.")
			return self.cleaned_data