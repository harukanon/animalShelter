from .models import Species, Breed
from django import forms

class adoptionForm(forms.Form):
    firstName = forms.CharField(label='firstName', max_length=32, required=True)
    lastName = forms.CharField(label='lastName', max_length=32, required=True)
    userDateOfBirth = forms.DateField(label='userDateOfBirth', required=True)
    email = forms.EmailField(label='email', required=True)
    phone = forms.CharField(label='phone', required=True)
    species = forms.ChoiceField(label='species', choices=[Species], required=True)
    breed = forms.ChoiceField(label='breed', choices=[Breed], required=True)
    meetingDate = forms.DateField(label='meetingDate', required=True)