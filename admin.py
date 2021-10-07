from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from .models import User, Group
from django.contrib.auth.models import Group as ContribGroup

admin.site.register(User, UserAdmin)

admin.site.unregister(ContribGroup)

admin.site.register(Group, GroupAdmin)

