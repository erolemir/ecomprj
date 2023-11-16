from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Kullanıcı Adı","size":"50"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"placeholder":"Email","size":"50"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Şifre","size":"50"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Şireyi Tekrarlayınız","size":"50"}))
    
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')