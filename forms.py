from django import forms
from .models import TougshireAuthUser

class ProfileForm(forms.ModelForm):
    class Meta:
        model = TougshireAuthUser
        fields = [
            'username',
            'email',
            'display_name'
        ]
