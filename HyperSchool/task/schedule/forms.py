from django import forms
from django.forms import ModelForm
from .models import *


class SearchForm(forms.Form):
    q = forms.CharField(max_length=100, required=True, label="Search",
        widget=forms.TextInput(attrs={'placeholder': 'Enter course name'}))

class StudentRegisterModelForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label="Name",
                           widget=forms.TextInput(attrs={"placeholder": "Enter student's name"}))
    surname = forms.CharField(max_length=100, required=True, label="Surname",
                              widget=forms.TextInput(attrs={'placeholder': "Enter student's surname"}))
    age = forms.IntegerField(required=True, label="Age")
    course = forms.ModelChoiceField(queryset=Course.objects.all())

