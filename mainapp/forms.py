from cProfile import label
from dataclasses import field
from django import forms

from mainapp.models import Snippet
from .models import Snippet

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(label='E-Mail')
    phone = forms.NumberInput()
    subject = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)

class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ('name', 'body')