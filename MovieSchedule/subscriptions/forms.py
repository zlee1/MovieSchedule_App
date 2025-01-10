from django import forms
from django.core.exceptions import ValidationError
import re

def validate_zip_code(zip_code):
    if(not re.match(r'[0-9]{5}', zip_code)):
        raise ValidationError('Invalid zip code.')

class TheaterSearchForm(forms.Form):
    zip_code = forms.CharField(max_length=5, label='Zip Code', validators=[validate_zip_code])