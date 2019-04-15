'''
Created on Apr 7, 2019

@author: S528358
'''
from django.urls import path
from .views import (
    Animal_list,
    Animal_detail,
    Animal_create,
    Animal_update,
    Animal_delete)
app_name = 'MarineAnimals'
urlpatterns = [   
    path('', Animal_list,name='Animal_list'),
    path('create/', Animal_create),
    path('<str:slug>/', Animal_detail),
    path('<str:slug>/update/', Animal_update),
    path('<str:slug>/delete/', Animal_delete),
    
    
    
#     path('animals/<str:slug>/update', Animal_update),
#     path('animals/<str:slug>/delete', Animal_delete),
    
]
