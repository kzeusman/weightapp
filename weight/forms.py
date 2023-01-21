from django.forms import ModelForm
from .models import Weight
from django import forms

class WeightForm(ModelForm):
	class Meta:
		model = Weight
		fields = ['weight','created','memo','important']

