'''
Created on Apr 7, 2019

@author: S528358
'''
from django.urls import path, re_path
from . import views
app_name = 'articles'
urlpatterns = [   
    path('', views.article_list, name = 'article_list'),
    
]
