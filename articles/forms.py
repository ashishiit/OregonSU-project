'''
Created on Apr 7, 2019

@author: S528358
'''
from django import forms
from . import models

class CreateEntry(forms.ModelForm):
    class Meta:
        model = models.MarineAnimals
        fields = ['title', 'body','pic']