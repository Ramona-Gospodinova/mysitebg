from django.forms import ModelForm
from .models import Case
from django import forms
from tinymce.widgets import TinyMCE
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

class CaseForm(ModelForm):
    description = forms.CharField(
        widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Case
        fields = '__all__'


class ContactForm(forms.Form):
    name = forms.CharField(label='Име', max_length=100)
    email = forms.EmailField(label='Имейл')
    message = forms.CharField(label='Съобщение', widget=forms.Textarea)
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

    def custom_label_tag(self, field_name):
        return self[field_name].label_tag(attrs={"class": "form-label"})