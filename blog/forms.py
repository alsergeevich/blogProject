from django import forms
from django.forms import Textarea
from captcha.fields import CaptchaField

from .models import *


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('content',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['content'].widget = Textarea(attrs={'row': 5, 'cols': 60})


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'cools': 60, 'rows': 5, 'class': 'form-control'}))
    captcha = CaptchaField(label='Я не робот')
