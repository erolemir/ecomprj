from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterForm(UserCreationForm):
    
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Kullanıcı Adı","size":"50"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"placeholder":"Email","size":"50"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Şifre","size":"50"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Şireyi Tekrarlayınız","size":"50"}))
    
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
class ProfileForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Ad Soyad","size":"50"}))
    bio = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Bio","size":"50"}))
    phone = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Telefon","size":"50"}))
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={"accept": "image/*"}))
    class Meta:
        model = Profile
        fields = ['full_name','image','bio', 'phone']

