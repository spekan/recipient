from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.messages import constants as messages

from .forms import UserForm, ChangePasswordForm
from .models import cardRecipient, CustomUser


class MainView(TemplateView):
    template_name = 'main/index.html'
    
    def get_auth(self, request):
        return render(request, self.template_name)

class LoginFormView(FormView):
    form_class = AuthenticationForm
    success_url = "login"
    template_name = 'main/login.html'
    
    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)
    
    def form_invalid(self, form):
        form.add_error(None, u'Неверное имя пользователя или пароль');
        return super(LoginFormView, self).form_invalid(form)

class LogoutView(TemplateView):
    template_name = "main/logout.html"

def recipients(request):
    return render(request, 'main/recipients.html', {'title': 'Список проживающих'})

def report(request):
    data = {
        'title': 'Отчет',

    }
    return render(request, 'main/report.html', data)

class UserView(TemplateView):

    template_name = 'mian/specialist.html'

    def get_u(self, request):
        try:
            return render(CustomUser.objects.get(pk=request))
        except:
            user_data = CustomUser.objects.all()
            return render('\n'.join([user.username for user in user_data]))
        # Вернуть информацию о юзере если был передан id юзера
        # Иначе вернуть список всех юзеров и информацию о них
        # ПОдробнее в Django ORM get/filter
        # from ... import User
        # user_data = User.object.get(id=request.GET.get('user_id'))
        # user_data = User.object.filter(...)

    def post(self, request):
        submitbutton = request.POST.get("OK")
        firstname=''
        lastname=''
        passWord=''
        user_name = ''
        form= UserForm(request.POST or None)
        if form.is_valid():
            user_name=form.cleaned_data.get("user_name")
            firstname=form.cleaned_data.get("firstname")
            lastname=form.cleaned_data.get("lastname")
            passWord=form.cleaned_data.get("passWord")
            new_user = CustomUser.objects.create(username=user_name,first_name=firstname, last_name=lastname, password=passWord, is_staff=True)
            new_user.save()
        # Создать пользователя по данным с фронта
        # name = request.data.get('name')
        # остальные поля пользователя
        # user_to_create = User(name=name, phone=phone)
        # Провалидировать данные - необязательно
        # user_to_create.save()

    def put(self, request):
        submitbutton = request.POST.get("OK")
        if request.method=="POST":
            password =request.user.password
            username=request.user.username
            form = ChangePasswordForm(request.POST or None)
            c_password=form.cleaned_data.get("current_password")
            new_password=form.cleaned_data.get("new_password")
            r_new_password=form.cleaned_data.get("retype_new_password")
            user = authenticate(username=username, password=c_password)
        if user is not None:
            if new_password==r_new_password:
                user = CustomUser.objects.get(username=username)
                user.set_password(new_password)
                user.save()
                messages.info(request,"Пароль изменен")
            else:
                messages.info(request,"Пароли не совпадают")
        else:
            messages.info(request,"Неверный пароль")
        # user_to_update = User.object.get(id=request.GET.get('user_id'))
        # user_to_update.name = request.data.get('name')
        # user_to_update.save()
    
    def delete(self, request):
        try:
            CustomUser.objects.filter(username=request).delete()     
            messages.info(request,"Успешно удален")       
        except:
            messages.info(request,"Возможно не существует")