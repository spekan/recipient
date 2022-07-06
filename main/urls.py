from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.MainView.as_view(), name='index'),
    path('recipients/', views.recipients, name='recipients'),
    path('report/', views.report, name='report'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginFormView.as_view(), name='login'),
    path('specialists/', views.all_specialists, name="all_specialists"),
    path('specialists/<int:customuser_id>/', views.UserView.get_u, name='some_specialist'),
    path('specialists/<int:customuser_id>/changepassword/', views.changepassword, name='changepassword'),
    path('specialists/<int:customuser_id>/delete/', views.UserView.delete, name='delete'),
]