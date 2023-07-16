from django import forms
from .models import TougshireAuthUser
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = TougshireAuthUser
        fields = [
            'username', 
            'email', 
            'display_name',
            'password1', 
            'password2'
        ]
        

class ProfileForm(forms.ModelForm):
    class Meta:
        model = TougshireAuthUser
        fields = [
            'username',
            'email',
            'display_name'
        ]
