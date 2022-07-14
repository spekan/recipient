from dataclasses import field, fields
from re import T
from django import forms
from django.forms import TextInput, DateInput, Textarea
from .models import CustomUser

class UserForm(forms.Form):
    user_name = forms.CharField(required=True, max_length=20, widget=TextInput(attrs={'type':'text','class': 'form-control','placeholder': 'Введите логин'}))
    firstname = forms.CharField(required=True, max_length=15, widget=TextInput(attrs={'type':'text','class': 'form-control','placeholder': 'Введите имя'}))
    lastname = forms.CharField(required=True, max_length=25, widget=TextInput(attrs={'type':'text','class': 'form-control','placeholder': 'Введите фамилию'}))
    passWord = forms.CharField(required=True, max_length=25, widget=TextInput(attrs={'type':'password','class': 'form-control','placeholder': 'Введите пароль'}))
    class Meta:
        fields = ['user_name', 'firstname', 'lastname', 'passWord']

class ChangePasswordForm(forms.Form):
    new_password = forms.CharField(required=True, max_length=25, widget=TextInput(attrs={'type':'password','class': 'form-control','placeholder': 'Введите новый пароль'}))
    retype_new_password = forms.CharField(required=True, max_length=25, widget=TextInput(attrs={'type':'password','class': 'form-control','placeholder': 'Введите новый пароль'}))
    class Meta:
        fields = ['new_password', 'retype_new_password']

class LoginForm(forms.Form):
    user_name = forms.CharField(max_length=20, widget=TextInput(attrs={'type':'text','class': 'form-control','placeholder': 'Введите логин'}))
    passWord = forms.CharField(max_length=25, widget=TextInput(attrs={'type':'password','class': 'form-control','placeholder': 'Введите пароль'}))
    class Meta:
        fields = ['user_name', 'passWord']

class cardRecipientForm(forms.Form):
    genderChoices=(
        ('М', 'М'),
        ('Ж', 'Ж'),
    )
    residenceChoices=(
        ('Ж', 'Ж'),
        ('П', 'П'),
    )
    reasonChoices=(
        ('НЕТ', 'НЕТ'),
        ('Продлен договор', 'Продлен договор'),
        ('Смерть', 'Смерть'),
        ('Решение жилищного вопроса', 'Решение жилищного вопроса'),
        ('Нарушение режима', 'Нарушение режима'),
        ('Оформление в др. соц. учреждения', 'Оформление в др. соц. учреждения'),
        ('Прочее', 'Прочее'),
    )
    socialStatusChoices=(
        ('БОМЖ', 'БОМЖ'),
        ('Не бездомный', 'Не бездомный'),
    )
    mlsChoices=(
        ('НЕТ', 'НЕТ'),
        ('МЛС', 'МЛС'),
    )
    disableChoices=(
        ('НЕТ', 'НЕТ'),
        ('ИНВ 1гр', 'ИНВ 1гр'),
        ('ИНВ 2гр', 'ИНВ 2гр'),
        ('ИНВ 3гр', 'ИНВ 3гр'),
    )
    disableAgeChoices=(
        ('НЕТ', 'НЕТ'),
        ('18-35 лет', '18-35 лет'),
        ('35-60 лет', '35-60 лет'),
        ('старше 60 лет', 'старше 60 лет'),
    )
    pensionerChoices=(
        ('НЕТ', 'НЕТ'),
        ('Пенс', 'Пенс'),
    )
    pensionerAgeChoices=(
        ('НЕТ', 'НЕТ'),
        ('до 54 лет', 'до 54 лет'),
        ('55-74 лет', '55-74 лет'),
        ('старше 75 лет', 'старше 75 лет'),
    )
    narcPndChoices=(
        ('НЕТ', 'НЕТ'),
        ('На учете', 'На учете'),
        ('В диспансере', 'В диспансере'),
    )
    employmentChoices=(
        ('Работает', 'Работает'),
        ('Не работает', 'Не работает'),
    )
    fio = forms.CharField(required=True, max_length=20, widget=TextInput(attrs={'type':'text','class': 'form-control'}))
    date_of_birthsday = forms.DateField(required=True, widget=DateInput(attrs={'class':'form=control'}))
    gender = forms.ChoiceField(required=True, choices=genderChoices)
    date_of_appeal = forms.DateField(required=True, widget=DateInput(attrs={'class':'form=control'}))
    date_end = forms.DateField(required=False, widget=DateInput(attrs={'class':'form=control'}))
    residence = forms.ChoiceField(required=True, choices=residenceChoices)
    specialist = forms.ModelChoiceField(required=True, queryset=CustomUser.objects.filter().values('last_name'))
    fluorography = forms.DateField(required=True, widget=DateInput(attrs={'class':'form=control'}))
    reason_end = forms.ChoiceField(required=True, choices=reasonChoices)
    period_time_begin = forms.DateField(required=True, widget=DateInput(attrs={'class':'form=control'}))
    period_time_end = forms.DateField(required=True, widget=DateInput(attrs={'class':'form=control'}))
    social_status = forms.ChoiceField(required=True, choices=socialStatusChoices)
    mls = forms.ChoiceField(required=True, choices=mlsChoices)
    mls_begin = forms.DateField(required=False, widget=DateInput(attrs={'class':'form=control'}))
    mls_end = forms.DateField(required=False, widget=DateInput(attrs={'class':'form=control'}))
    disabled = forms.ChoiceField(required=True, choices=disableChoices)
    age_disabled = forms.ChoiceField(required=True, choices=disableAgeChoices)
    pensioner = forms.ChoiceField(required=True, choices=pensionerChoices)
    age_pensioner = forms.ChoiceField(required=True, choices=pensionerAgeChoices)
    narkology = forms.ChoiceField(required=True, choices=narcPndChoices)
    pnd = forms.ChoiceField(required=True, choices=narcPndChoices)
    employment = forms.ChoiceField(required=True, choices=employmentChoices)
    number_room = forms.IntegerField(required=True, max_value=99)
    photo = forms.ImageField(required=False)
    comment = forms.CharField(required=False, widget=Textarea(attrs={'class': 'form-control'}))
    class Meta:
        fields = [
            'fio','date_of_birthsday','gender','date_of_appeal','date_end','residence','specialist','fluorography',
            'reason_end','period_time_begin','period_time_end','social_status','mls','mls_begin','mls_end','disabled',
            'age_disabled','pensioner','age_pensioner','narkology','pnd','employment','number_room','comment',
            ]