from django import forms

class adoptionForm(forms.Form):
    firstName = forms.CharField(min_length=1, max_length=32)
    lastName = forms.CharField(min_length=1, max_length=32)
    date

