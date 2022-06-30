from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='index'),
    path('recipients/', views.recipients, name='recipients'),
    path('report/', views.report, name='report'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginFormView.as_view(), name='login'),
    path('specialists/', views.UserView.as_view(), name="specialists")
]