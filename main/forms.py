from django import forms
from django.forms import TextInput

class UserForm(forms.Form):
    user_name = forms.CharField(max_length=20)
    firstname = forms.CharField(max_length=15)
    lastname = forms.CharField(max_length=25)
    passWord = forms.CharField(max_length=25)

class ChangePasswordForm(forms.Form):
    new_password = forms.CharField(max_length=25, widget=TextInput(attrs={'type':'password','class': 'form-control','placeholder': 'Введите новый пароль'}))
    retype_new_password = forms.CharField(max_length=25, widget=TextInput(attrs={'type':'password','class': 'form-control','placeholder': 'Введите новый пароль'}))
    class Meta:
        fields = ['new_password', 'retype_new_password']