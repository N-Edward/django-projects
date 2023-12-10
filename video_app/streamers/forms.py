from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Profile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        feilds = ['username','email','password1','password2']
        
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model= User
        feilds = ['username','email']
        
class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image'] 