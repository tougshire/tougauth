from .models import TougshireAuthUser, TougshireAuthGroup
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext, gettext_lazy as _


class TougshireAuthUserAdmin(UserAdmin):
    #copies of UserAdmin fieldsets and search_fields, but with display_name added, and a modified list_display
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'display_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display=['name', 'username', 'email']
    search_fields = ('username', 'first_name', 'last_name', 'display_name', 'email')

admin.site.register(TougshireAuthUser, TougshireAuthUserAdmin)

admin.site.unregister(Group)

class TougshireAuthGroupAdmin(GroupAdmin):
    pass

admin.site.register(TougshireAuthGroup, TougshireAuthGroupAdmin)
