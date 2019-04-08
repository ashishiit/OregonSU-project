from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import MarineAnimals
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from django.utils.text import slugify
from articles.forms import CreateEntry
# Create your views here.
# @login_required(login_url='/accounts/login')
def article_list(request):
    obj = MarineAnimals.objects.all().order_by('time')
    return render(request, 'articles/article_list.html', {'obj':obj})