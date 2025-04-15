from django import forms

class adoptionForm(forms.Form):
    name = forms.CharField()