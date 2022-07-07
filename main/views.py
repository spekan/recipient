from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.messages import constants as messages
from django.http import Http404
from .forms import LoginForm, UserForm, ChangePasswordForm
from .models import cardRecipient, CustomUser


class MainView(TemplateView):
    template_name = 'main/index.html'
    
    def get_auth(self, request):
        return render(request, self.template_name)

def login(request):
    template_name = 'main/login'
    user_name = ''
    passWord = ''
    action_detail = ''
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid:
            user_name = form.cleaned_data.get('user_name')
            passWord = form.cleaned_data.get('passWord')
            try:
                user = CustomUser.objects.get(username=user_name, password=passWord)
                # Необходимо авторизировать пользователя user
                return redirect('/')
            except:
                action_detail = 'Неверное имя пользователя или пароль'
    context={
            'title': 'Войдите в аккаунт',
            'form': form,
            'action_detail': action_detail,
        }
    return(request, template_name, context)


def logout(request):
    # Необходимо осуществить выход из аккаунта
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
            'context': user_name
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
        if form.is_valid:
            new_password=form.cleaned_data.get('new_password')
            r_new_password=form.cleaned_data.get('retype_new_password')
            if new_password==r_new_password:
                current_user.set_password(new_password)
                current_user.save()
                messages.INFO("Пароль успешно изменен")
                return redirect('/specialists/')
            else:
                text_action = "Пароли не совпадают"
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
    form = UserForm()
    context ={
        'title': 'Создание пользователя', 
        'form': form,
    }
    return render(request, template_name, context)

def delete(request, customuser_id):
        try:
            CustomUser.objects.filter(id=customuser_id).delete()        
        except:
            pass
        return redirect('/specialists/')

class UserView(TemplateView):

    template_name = 'main/some_specialist.html'    
    
    def get_u(request, customuser_id):
        try:
            user_name = CustomUser.objects.get(pk=customuser_id)
        except CustomUser.DoesNotExist:
            raise Http404("Пользователь не найден")
        return render(request, UserView.template_name, {'user_name': user_name})
        # Вернуть информацэто шифраию о юзере если был передан id юзера
        # Иначе вернуть список всех юзеров и информацию о них
        # ПОдробнее в Django ORM get/filter
        # from ... import User
        # user_data = User.object.get(id=request.GET.get('user_id'))
        # user_data = User.object.filter(...)