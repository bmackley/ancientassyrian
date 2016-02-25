from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login
from homePage import models as m
from . import templater

def process_request(request):
  charForm = CreateCharForm()
  if request.method == "POST":
    charForm = CreateCharForm(request.POST)
    if charForm.is_valid():
      new_char = m.Character()
      new_char.line = charForm.cleaned_data['line']
      new_char.Sign = charForm.cleaned_data['sign']
      new_char.note = charForm.cleaned_data['note']
      new_char.save()

  tvars = {
    "charForm" : charForm,
  }
  return templater.render_to_response(request, 'create_chars.html', tvars)

class CreateCharForm(forms.Form):
  sign = forms.ModelChoiceField(queryset=m.Sign.objects.all(), to_field_name="filepath")
  line = forms.ModelChoiceField(queryset=m.Line.objects.all(), to_field_name="id")
  note = forms.CharField(label='Note', widget=forms.TextInput(attrs={'class':'form-control'}))
