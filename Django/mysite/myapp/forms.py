# forms.py
from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label='Ваше имя', max_length=100)