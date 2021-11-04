from django import forms
from . import models

class createParameter(forms.ModelForm):
    minPrice = forms.CharField(required=False)
    maxPrice = forms.CharField(required=False)
    minYear = forms.CharField(required=False)
    maxYear = forms.CharField(required=False)
    minOdometer = forms.CharField(required=False)
    maxOdometer = forms.CharField(required=False)
    condition = forms.CharField(required=False)
    miles = forms.CharField(required=False)
    postalCode = forms.CharField(required=False)
    carModel = forms.CharField(required=False)