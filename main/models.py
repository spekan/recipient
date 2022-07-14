from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(max_length=20, blank=False, null=False, unique=True, verbose_name='Логин')
    first_name = models.CharField(max_length=20, blank=False, null=False, verbose_name='Имя')
    last_name = models.CharField(max_length=20, blank=False, null=False, verbose_name='Фамилия')
    password = models.CharField(max_length=20, blank=False, null=False, verbose_name='Пароль')

    def __str__(self):
        return self.username


class cardRecipient(models.Model):
    class genderChoices(models.TextChoices):
        c1 = 'М', _('М')
        c2 = 'Ж', _('Ж')
    class residenceChoices(models.TextChoices):
        c1 = 'Ж', _('Ж')
        c2 = 'П', _('П')
    class reasonChoices(models.TextChoices):
        c1 = 'НЕТ', _('НЕТ')
        c2 = 'Продлен договор', _('Продлен договор')
        c3 = 'Смерть', _('Смерть')
        c4 = 'Решение жилищного вопроса', _('Решение жилищного вопроса')
        c5 = 'Нарушение режима', _('Нарушение режима')
        c6 = 'Оформление в др. соц. учреждения', _('Оформление в др. соц. учреждения')
        c7 = 'Прочее', _('Прочее')
    class socialStatusChoices(models.TextChoices):
        c1 = 'БОМЖ', _('БОМЖ')
        c2 = 'Не бездомный', _('Не бездомный')
    class mlsChoices(models.TextChoices):
        c1 = 'НЕТ', _('НЕТ')
        c2 = 'МЛС', _('МЛС')
    class disableChoices(models.TextChoices):
        c1 = 'НЕТ', _('НЕТ')
        c2 = 'ИНВ 1гр', _('ИНВ 1гр')
        c3 = 'ИНВ 2гр', _('ИНВ 2гр')
        c4 = 'ИНВ 3гр', _('ИНВ 3гр')
    class disableAgeChoices(models.TextChoices):
        c1 = 'НЕТ', _('НЕТ')
        c2 = '18-35 лет', _('18-35 лет')
        c3 = '35-60 лет', _('35-60 лет')
        c4 = 'старше 60 лет', _('старше 60 лет')
    class pensionerChoices(models.TextChoices):
        c1 = 'НЕТ', _('НЕТ')
        c2 = 'Пенс', _('Пенс')
    class pensionerAgeChoices(models.TextChoices):
        c1 = 'НЕТ', _('НЕТ')
        c2 = 'до 54 лет', _('до 54 лет')
        c3 = '55-74 лет', _('55-74 лет')
        c4 = 'старше 75 лет', _('старше 75 лет')
    class narcPndChoices(models.TextChoices):
        c1 = 'НЕТ', _('НЕТ')
        c2 = 'На учете', _('На учете')
        c3 = 'В диспансере', _('В диспансере')
    class employmentChoices(models.TextChoices):
        c1 = 'Работает', _('Работает')
        c2 = 'Не работает', _('Не работает')
    fio = models.CharField(max_length=80, blank=False, null=True)
    date_of_birthsday = models.DateField(blank=False, null=True)
    gender = models.CharField(max_length=1, choices=genderChoices.choices, default=genderChoices.c1)
    date_of_appeal = models.DateField(blank=False, null=True)
    date_end = models.DateField(blank=True, null=True)
    residence = models.CharField(max_length=1, choices=residenceChoices.choices, default=residenceChoices.c1)
    specialist = models.ForeignKey(CustomUser, on_delete=models.PROTECT, blank=False, null=True)
    fluorography = models.DateField(blank=False, null=True)
    reason_end = models.CharField(max_length=33, choices=reasonChoices.choices, default=reasonChoices.c1)
    period_time_begin = models.DateField(blank=False, null=True)
    period_time_end = models.DateField(blank=False, null=True)
    social_status = models.CharField(max_length=14, choices=socialStatusChoices.choices, default=socialStatusChoices.c1)
    mls = models.CharField(max_length=3, choices=mlsChoices.choices, default=mlsChoices.c1)
    mls_begin = models.DateField(blank=True, null=True)
    mls_end = models.DateField(blank=True, null=True)
    disabled = models.CharField(max_length=7, choices=disableChoices.choices, default=disableChoices.c1)
    age_disabled = models.CharField(max_length=13, choices=disableAgeChoices.choices, default=disableAgeChoices.c1)
    pensioner = models.CharField(max_length=4, choices=pensionerChoices.choices, default=pensionerChoices.c1)
    age_pensioner = models.CharField(max_length=13, choices=pensionerAgeChoices.choices, default=pensionerAgeChoices.c1)
    narkology = models.CharField(max_length=12, choices=narcPndChoices.choices, default=narcPndChoices.c1)
    pnd = models.CharField(max_length=12, choices=narcPndChoices.choices, default=narcPndChoices.c1)
    employment = models.CharField(max_length=11, choices=employmentChoices.choices, default=employmentChoices.c1)
    number_room = models.CharField(max_length=3, blank=False, null=True)
    photo = models.ImageField()
    comment = models.TextField(blank=True, null='')
