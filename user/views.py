from django.shortcuts import render,redirect
from user.forms import UserRegisterForm
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as django_login, logout

# Create your views here.
import logging

logger = logging.getLogger(__name__)


def register_view(request):
    if request.method=="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hoşgeldin {username}, hesabın başarıyla oluşturuldu.")
            new_user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1'])
            login = (request,new_user)
            return redirect("core:index")
    else :
        form = UserRegisterForm()
        
    context ={
        'form':form,
    }
    return render(request,"user/sign-up.html",context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            django_login(request,user)
            messages.success(request,"Giriş Başarılı.")
            return redirect('core:index')
        else:
            messages.warning(request,"Login Hatası! Kullanıcı adı veya şifre yanlış.")
            return redirect ('user:sign-in')
            # Return an 'invalid login' error message.
    return render(request, 'user/sign-in.html')

def logout_view(request):
    logout(request)
    return redirect("user:sign-in")