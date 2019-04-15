from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.db import models
# Create your models here.
User = settings.AUTH_USER_MODEL
class Animal(models.Model):
    user = models.ForeignKey(User, default = 1, null = True, on_delete= models.SET_NULL)
    title = models.CharField(max_length = 100)
    slug = models.SlugField(unique = True)
    content = models.TextField() 
   
    
    def __str__(self):
        return self.title
    def snippet(self):
        return self.body[:30]+'...'
    
    def get_absolute_url(self):
        return f"{self.slug}"
    
    def get_update_url(self):
        return f"{self.slug}/update"
    
    def get_delete_url(self):
        return f"{self.slug}/delete"