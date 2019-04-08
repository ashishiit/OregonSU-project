'''
Created on Apr 7, 2019

@author: S528358
'''
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.utils.text import slugify
# Create your models here.
class MarineAnimals(models.Model):
    title = models.CharField(max_length = 100)
    body = models.TextField()
    slug = models.SlugField(unique=True)
    time = models.DateTimeField(auto_now_add=True)
    pic = models.ImageField(null=True, blank=True)    
#     authorid = models.ForeignKey(User,models.SET_NULL,blank=True,null=True)   
    
    def __str__(self):
        return self.title
    def snippet(self):
        return self.body[:30]+'...'
    
    def get_absolute_url(self):
        return '/accounts/%s' %self.authorid