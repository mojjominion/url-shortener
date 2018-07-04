from django import forms
from .validators import validate_url, alphanumeric

class UrlForm(forms.Form):
    url        = forms.CharField(label='URL', max_length=220, validators=[validate_url])
    short_key  = forms.CharField(label='Custom URL (Alphanumeric only)',min_length=6, max_length=15, required=False, validators=[alphanumeric])
    expire     = forms.IntegerField(label='Will expires in (minutes)', widget=forms.TextInput(attrs={'type':'number', 'min':1, 'value':1, 'placeholder':'in minutes'}))