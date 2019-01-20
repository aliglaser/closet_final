from django import forms
from django.shortcuts import get_object_or_404
#from crispy_forms.helper import FormHelper
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




 
 
class TestForm(forms.Form):
    """
    Form to upload the screenshot of a webpage
    """
 
    image_data = forms.CharField(widget=forms.HiddenInput(), required=False)
 
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = "agreement_form"
        self.helper.form_method = 'post'
 
        super(TestForm, self).__init__(*args, **kwargs)

Clothes_Formset = forms.modelformset_factory(
	models.Clothes, 
	form=ClothesForm
)