from django import forms
from django.shortcuts import get_object_or_404
from . import models


class PhotoForm(forms.ModelForm):
	class Meta:
		model = models.Photo
		fields = [
			'file',
		]


class ClothesForm(forms.ModelForm):
	class Meta:
		model = models.Clothes
		fields = [
			'category', 
			'season', 
			'color', 
			'pattern',
			'photoid',
		]


Clothes_Formset = forms.modelformset_factory(
	models.Clothes, 
	form=ClothesForm
)