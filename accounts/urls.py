from django.urls import path, include
from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('accounts/register', views.register, name='register'),
    path('', views.user_login, name='login'),
    path('accounts/login', views.user_login, name='login'),
    path('accounts/restricted', views.restricted, name='restricted'),
    path('accounts/logout', views.user_logout, name='logout'),
    path('accounts/changePassword', views.change_password, name='changepwd'),
]