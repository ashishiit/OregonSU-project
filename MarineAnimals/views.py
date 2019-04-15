from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Animal
from django.utils.text import slugify
from .forms import CreateAnimalModel
# Create your views here.
# @login_required(login_url='/accounts/login')
def Animal_detail(request, slug):
    obj = get_object_or_404(Animal, slug = slug)
    print(obj.slug)
    context = {"obj":obj}
    return render(request, "detail.html", context)

def Animal_list(request, slug=None):
           
    querySet = Animal.objects.all()
    context = {"obj_list":querySet}
    return render(request, "animal_list.html", context)

@staff_member_required
def Animal_create(request):
    form = CreateAnimalModel(request.POST or None)
    if form.is_valid():
        form.save()
        form = CreateAnimalModel()
        return redirect("/animals")
    context = {'form':form}
    return render(request, 'form.html', context)

@staff_member_required
def Animal_update(request, slug):
    obj = get_object_or_404(Animal, slug = slug)
    print(obj)
    form = CreateAnimalModel(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect("/animals")
    context = {"form":form, "obj":obj}
    return render(request, "form.html", context)

@staff_member_required
def Animal_delete(request, slug):
    obj = get_object_or_404(Animal, slug = slug)
    if request.method == 'POST':
        obj.delete()
        return redirect("/animals")
    context = {'obj':obj}
    return render(request, "delete.html", context)