'''
Created on Apr 7, 2019

@author: S528358
'''
from django.http import HttpResponse
from django.shortcuts import render

def about(request):
#     return HttpResponse('about')
    title = "this is About page"
    return render(request, "homepage.html", {'title':title})

def homepage(request):
    title = "Home Page"
    context = {"title":title}
    if request.user.is_authenticated:
        context = {"title":title, "my_list":[1,2,3]}
    return render(request, "homepage.html", context)