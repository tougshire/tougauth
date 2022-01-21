from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='tougshire_auth/login.html'), name='login', ),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/', views.ProfileDetail.as_view(), name='tougshire_user_profile'),
    path('profile/update', views.ProfileUpdate.as_view(), name='tougshire_user_profile_update'),
    path('profile/update', views.ProfileUpdate.as_view(), name='profile'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='tougshire_auth/password_change_form.html'),  name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeView.as_view(template_name='tougshire_auth/tougshire_auth/password_change_done.html'), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='tougshire_auth/password_reset_form.html'),  name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetView.as_view(template_name='tougshire_auth/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='tougshire_auth/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='tougshire_auth/password_reset_done.html'), name='password_reset_complete'),
]

