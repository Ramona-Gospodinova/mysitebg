from django.forms import ModelForm
from .models import Case
from django import forms
from tinymce.widgets import TinyMCE


class CaseForm(ModelForm):
    description = forms.CharField(
        widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Case
        fields = '__all__'
