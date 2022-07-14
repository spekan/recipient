from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.messages import constants as messages
from django.http import Http404
from .forms import LoginForm, UserForm, ChangePasswordForm, cardRecipientForm
from .models import cardRecipient, CustomUser


class MainView(TemplateView):
    template_name = 'main/index.html'
    
    def get_auth(self, request):
        return render(request, self.template_name)

def login_view(request):
    template_name = 'main/login.html'
    action_detail = ''
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('user_name')
            password = form.cleaned_data.get('passWord')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                action_detail = 'Неверное имя пользователя или пароль'
    else:
        form = LoginForm()
    context={
            'title': 'Вход в аккаунт',
            'form': form,
            'action_detail': action_detail,
        }
    return render(request, template_name, context)


def logout_view(request):
    logout(request)
    return redirect('/')

def recipients(request):
    return render(request, 'main/recipients.html', {'title': 'Список проживающих'})

def report(request):
    data = {
        'title': 'Отчет',

    }
    return render(request, 'main/report.html', data)

def all_specialists(request):
        user_name = CustomUser.objects.values('id','first_name', 'last_name')
        context={
            'context': user_name,
            'title': 'Пользователи'
        }
        return render(request, 'main/specialist.html', context=context)

def changepassword(request, customuser_id):
    current_user = CustomUser.objects.get(id=customuser_id)
    template_name = 'main/changepassword.html'
    text_action = '' 
    new_password = ''
    r_new_password = '' 
    if request.method == "POST":
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            new_password=form.cleaned_data.get('new_password')
            r_new_password=form.cleaned_data.get('retype_new_password')
            if new_password==r_new_password:
                current_user.set_password(new_password)
                current_user.save()
                return redirect('/specialists/')
            else:
                text_action = "Пароли не совпадают"
    else:
        form = ChangePasswordForm()
    context ={
        'title': 'Смена пароля', 
        'form': form,
        'text_action' : text_action,
    }
    return render(request, template_name, context)

def add_user(request):
    template_name = 'main/add_user.html'
    firstname=''
    lastname=''
    passWord=''
    user_name = ''
    if request.method == "POST":
        form= UserForm(request.POST)
        if form.is_valid():
            user_name=form.cleaned_data.get("user_name")
            firstname=form.cleaned_data.get("firstname")
            lastname=form.cleaned_data.get("lastname")
            passWord=form.cleaned_data.get("passWord")
            new_user = CustomUser.objects.create(username=user_name,first_name=firstname, last_name=lastname, password=passWord, is_staff=True)
            new_user.set_password(passWord)
            new_user.save()
            return redirect('/specialists/')
    else:
        form = UserForm()
    context ={
        'title': 'Добавление клиента', 
        'form': form,
    }
    return render(request, template_name, context)

def delete(request, customuser_id):
        try:
            CustomUser.objects.filter(id=customuser_id).delete()        
        except:
            pass
        return redirect('/specialists/')

def all_recipients(request):
    template_name = 'main/recipients.html'
    clients = cardRecipient.objects.values('id', 'fio', 'date_of_birthsday')
    context={
        'context': clients,
        'title': 'Получатели социальных услуг',
    }
    return render(request, template_name, context)

def add_cardRecipient(request):
    template_name = 'main/add_card.html'
    if request.method == "POST":
        form= cardRecipientForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_card = cardRecipient.objects.create(fio= cd['fio'],date_of_birthsday=cd['date_of_birthsday'],gender=cd['gender'],date_of_appeal=cd['date_of_appeal'],
            date_end=cd['date_end'],residence= cd['residence'],specialist=cd['specialist'],fluorography=cd['fluorography'],reason_end= cd['reason_end'],
            period_time_begin=cd['period_time_begin'],period_time_end=cd['period_time_end'],social_status=cd['social_status'],mls=cd['mls'],mls_begin=cd['mls_begin'],
            mls_end=cd['mls_end'],disabled=cd['disabled'],age_disabled=cd['age_disabled'],pensioner=cd['pensioner'],age_pensioner=cd['age_pensioner'],
            narkology=cd['narkology'],pnd=cd['pnd'],employment=cd['employment'],number_room=cd['number_room'],comment=cd['comment'])
            new_card.save()
            return redirect('/recipients/')
    else:
        form = cardRecipientForm()
    context ={
        'title': 'Добавление клиента', 
        'form': form,
    }
    return render(request, template_name, context)

def get_r(request, cardrecipient_id):
    template_name = 'main/some_recipients.html'
    try:
        card = cardRecipient.objects.get(pk=cardrecipient_id)
    except cardRecipient.DoesNotExist:
        raise Http404("Клиент не найден")
    return render(request, template_name, {'card': card})

class UserView(TemplateView):

    template_name = 'main/some_specialist.html'    
    
    def get_u(request, customuser_id):
        try:
            user_name = CustomUser.objects.get(pk=customuser_id)
        except CustomUser.DoesNotExist:
            raise Http404("Пользователь не найден")
        return render(request, UserView.template_name, {'user_name': user_name})