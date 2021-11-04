from django import forms
from . import models

class createParameter(forms.ModelForm):
    class Meta:
        model = models.Parameters
        fields = ['minPrice','maxPrice',
        'minYear','maxYear','minOdometer','maxOdometer',
        'condition','miles','postalCode','carModel']