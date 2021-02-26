from django import forms
from django.forms import HiddenInput
from .models import Movie

class MovieForm(forms.ModelForm):
    
    class Meta:
        model=Movie
        fields=('url',)
        