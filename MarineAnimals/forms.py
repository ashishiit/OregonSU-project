'''
Created on Apr 7, 2019

@author: S528358
'''
from django import forms

from . models import Animal
class CreateAnimal(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget = forms.Textarea)
    
class CreateAnimalModel(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['title', 'slug', 'content']
        
    def clean_title(self, *args, **kwargs):
        instance = self.instance
        title = self.cleaned_data.get('title')
        QuerySet = Animal.objects.filter(title__iexact=title)
        if instance is not None:
            QuerySet = QuerySet.exclude(pk=instance.pk)
        if QuerySet.exists():
            raise forms.ValidationError("title exists. Try another")
        return title