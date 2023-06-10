from .models import TougshireAuthUser
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext, gettext_lazy as _


@admin.display(description="Active/Staff/Super")
def activestaffsuper(obj):
    return "{} / {} / {}".format(['No ', 'Yes'][obj.is_active], ['No ', 'Yes'][obj.is_staff], ['No ', 'Yes'][obj.is_superuser])

@admin.display(description="Groups")
def group_letters(obj):

    chars=''
    for group in obj.groups.all():
        chars = chars + group.name

    return chars


class GroupFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('groups')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'groups__id__exact'

    def lookups(self, request, model_admin):
        return  [(group.id,  group.__str__) for group in Group.objects.all()] + [('-', '-')]

    def queryset(self, request, queryset):

        if self.value():
            if self.value() == '-':
                return queryset.filter(groups__isnull=True)
            return queryset.filter(groups__id__exact=self.value())
        return queryset


class TougshireAuthUserAdmin(UserAdmin):
    # copies of UserAdmin fieldsets and search_fields, but with display_name added, and a modified list_display
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {
         'fields': ('first_name', 'last_name', 'display_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ['name', 'username', 'email', activestaffsuper, group_letters]
    search_fields = ('username', 'first_name',
                     'last_name', 'display_name', 'email')

    list_filter =  [filter for filter in UserAdmin.list_filter if filter != "groups"] + [GroupFilter,]

admin.site.register(TougshireAuthUser, TougshireAuthUserAdmin)

