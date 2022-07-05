from django import forms

class UserForm(forms.Form):
    user_name = forms.CharField(max_length=20)
    firstname = forms.CharField(max_length=15)
    lastname = forms.CharField(max_length=25)
    passWord = forms.CharField(max_length=25)

class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(max_length=25)
    new_password = forms.CharField(max_length=25)
    retype_new_password = forms.CharField(max_length=25)