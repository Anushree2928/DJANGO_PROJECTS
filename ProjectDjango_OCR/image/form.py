from django import forms
from .models import Image
from django.forms import ModelForm

class ImageForm (forms.ModelForm):
	class Meta:
		model = Image
		fields = ('caption','image')