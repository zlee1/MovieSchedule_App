from django import forms

class TheaterSearchForm(forms.Form):
    zip_code = forms.CharField(max_length=5, label='Zip Code')

    # class Meta:
    #     fields = ['zip_code']