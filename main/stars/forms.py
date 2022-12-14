from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField
from .models import *

class AddPostForm(forms.ModelForm):
      def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['cat'].empty_label = 'select category'

      class Meta:
            model = Stars
            #fields = '__all__'
            fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
            widgets = {
                  'title': forms.TextInput(attrs={'class': 'form-input'}),
                  'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
            }

      def clean_title(self):
           title = self.cleaned_data['title']
           if len(title) > 200:
                 raise ValidationError('Length above 200 characters')
           return title

class RegisterUserForm(UserCreationForm):
      username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': "form-input"}))
      email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': "form-input"}))
      password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
      password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

      class Meta:
            model = User
            fields = ('username', 'email', 'password1', 'password2')
            wiedgets = {
                  'username': forms.TextInput(attrs={'class': 'form-input'}),
                  'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
                  'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
                  }


class LoginUserForm(AuthenticationForm):
      username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': "form-input"}))
      password = forms.CharField(label='Password', widget=forms.TextInput(attrs={'class': "form-input"}))


class FeedbackForm(forms.Form):
      name = forms.CharField(label='Name', max_length=255)
      email = forms.CharField(label='Email')
      content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))

      captcha = CaptchaField()
