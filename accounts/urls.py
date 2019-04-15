'''
Created on Apr 15, 2019

@author: S528358
'''
from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views
from accounts.views import login_view, sign_up

app_name = 'accounts'
urlpatterns = [    
   path('sign_up',views.sign_up, name = "sign_up"),
    path('login',views.login_view, name = 'login_view'),
    ]