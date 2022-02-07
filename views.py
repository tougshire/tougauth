from django.core.exceptions import PermissionDenied
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from .models import TougshireAuthUser
from .forms import ProfileForm
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.conf import settings

class ProfileDetail(DetailView):
    model = TougshireAuthUser
    template_name = 'tougshire_auth/profile_detail.html'

    def get_object(self):
        if(self.request.user.pk):
            return self.request.user
        raise PermissionDenied

    def get_context_data(self, **kwargs):

        context_data = super().get_context_data(**kwargs)

        if hasattr(settings, 'TOUGSHIRE_AUTH_MENU_FILE'):
            context_data['menufile'] = settings.TOUGSHIRE_AUTH_MENU_FILE

        return context_data

class ProfileUpdate(UpdateView):
    model = TougshireAuthUser
    template_name = 'tougshire_auth/profile_form.html'
    form_class = ProfileForm
    def get_object(self):
        if(self.request.user.pk):
            return self.request.user
        raise PermissionDenied

    def get_success_url(self):
        return reverse_lazy('tougshire_user_profile')

    def get_context_data(self, **kwargs):

        context_data = super().get_context_data(**kwargs)

        if hasattr(settings, 'TOUGSHIRE_AUTH_MENU_FILE'):
            context_data['menufile'] = settings.TOUGSHIRE_AUTH_MENU_FILE

        return context_data
