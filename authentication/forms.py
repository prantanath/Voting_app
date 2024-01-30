from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *


class UserRegisterationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserRegisterationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = ''
        self.fields['name'].label = ''
        self.fields['password1'].label = ''
        self.fields['password2'].label = ''
        self.fields['name'].widget.attrs['placeholder'] = 'Name'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Re-enter Password'

    password1 = forms.CharField(label='Enter password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password',widget=forms.PasswordInput)

    class Meta:
        model = Employee
        fields = ("username","name", "password1", "password2")
        help_texts = {"username": None}


class UserAuthenticationForm(AuthenticationForm):
          
    def __init__(self, *args, **kwargs):
        super(UserAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = ''
        self.fields['password'].label = ''
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'

    password = forms.CharField(label='Enter password',widget=forms.PasswordInput)

    class Meta:
        model = Employee
        fields = ("username", "password")
        help_texts = {"username": None}