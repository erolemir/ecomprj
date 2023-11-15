from django.shortcuts import render
from user.forms import UserRegisterForm

# Create your views here.

def register_view(request):
    if request.method=="POST":
        form = UserRegisterForm()
        print("user registered")
    else :
        form = UserRegisterForm()
        
    context ={
        'form':form,
    }
    return render(request,"user/sign-up.html",context)