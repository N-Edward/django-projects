from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#creating custom forms
class SignupForm(UserCreationForm):
    class Meta:
        models = User
        fields = ['username','password1','password2']
        
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)