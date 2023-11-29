from django.shortcuts import get_object_or_404, render,redirect
from userauth.forms import UserRegisterForm,ProfileForm
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as django_login, logout
from .models import Profile
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from core.models import ProductReview
from django.contrib.auth.decorators import login_required
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

def profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        # Handle the case where the profile does not exist
        profile = None

    context = {'profile': profile}
    return render(request, 'user/userprofile.html', context)

def profile_update(request):
    
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES,instance=profile)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user=request.user
            new_form.save()
            messages.success(request, "Bilgileriniz Güncellendi")
            return redirect("user:profile")
    else:
        form = ProfileForm(instance=profile)

    context = {
        "form": form,
        "profile":profile,
    }
    return render(request, 'user/profile_edit.html', context)

def change_password(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user) # Important!
            messages.success(request,"Şifreniz Başarıyla Değiştirildi")
            return redirect('index')
        else:
            messages.error(request,"Please correct the error below.<br>"+str(form.errors))
            return redirect('user:change_password')
    else:
        form = PasswordChangeForm(request.user)
        return render(request,'user/change_password.html',{'form':form,"profile":profile})
    
@login_required(login_url='/login') # Check login
def comments(request):
    current_user = request.user
    comments = ProductReview.objects.filter(user_id=current_user.id)
    context = {'comments':comments}
    return render(request,'user/user_comments.html',context)

@login_required(login_url='/login') # Check login
def deletecomments(request,id):
    current_user = request.user
    ProductReview.objects.filter(id=id,user_id=current_user.id).delete()
    messages.success(request,"Yorumunuz Silinmiştir")
    return redirect('user:comments')

