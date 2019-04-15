from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('accounts:login_view')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/sign_up.html',{'form':form})

def login_view(request, slug=None):
   
#     print(request.GET.urlencode())
    if request.method == 'POST':
        print('login user',slug)
        print('login_view',request.user)
        print(request.POST)
        print('username' in request.POST)
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))            
            else:
                return redirect('MarineAnimals:Animal_list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})