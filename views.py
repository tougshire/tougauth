from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from .models import TougshireAuthUser

class ProfileDetail(DetailView):
    model = TougshireAuthUser
    template_name = 'tougshire_auth/profile_detail.html'

    def get_object(self):
        return self.request.user

class ProfileUpdate(UpdateView):
    model = TougshireAuthUser
    template_name = 'tougshire_auth/profile_form.html'
    fields=['username']
    def get_object(self):
        return self.request.user
