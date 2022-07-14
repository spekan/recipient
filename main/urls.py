from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.MainView.as_view(), name='index'),
    path('recipients/', views.all_recipients, name='recipients'),
    path('recipients/add', views.add_cardRecipient, name='add_recipients'),
    path('recipients/<int:cardrecipient_id>', views.get_r, name='some_recipients'),
    path('report/', views.report, name='report'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('specialists/', views.all_specialists, name="all_specialists"),
    path('specialists/add/', views.add_user, name='add_specialist'),
    path('specialists/<int:customuser_id>/', views.UserView.get_u, name='some_specialist'),
    path('specialists/<int:customuser_id>/changepassword/', views.changepassword, name='changepassword'),
    path('specialists/<int:customuser_id>/delete/', views.delete, name='delete'),
]