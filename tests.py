from .models import TougshireAuthGroup, TougshireAuthUser
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from django.shortcuts import get_object_or_404
from django.test import Client, TestCase

class TestUserAndGroup(TestCase):

    @classmethod
    def setUpTestData(cls):
        TougshireAuthUser.objects.create(username="usealpha")
        TougshireAuthGroup.objects.create(name="grualpha")

    def setUp(self):
        pass

    def test_user_exits(self):
        self.assertEqual(TougshireAuthUser.objects.count(), 1)

    def test_user_parameters(self):
        usealpha = TougshireAuthUser.objects.get(username='usealpha')
        self.assertEqual(usealpha.__str__(), 'usealpha')

    def test_user_can_have_perm(self):
        usealpha = TougshireAuthUser.objects.get(username='usealpha')
        usealpha.user_permissions.add(Permission.objects.get(codename='view_tougshireauthuser'))
        self.assertTrue(usealpha.has_perm('tougshire_auth.view_tougshireauthuser'))

    def test_user_can_lose_perm(self):
        usealpha = TougshireAuthUser.objects.get(username='usealpha')
        usealpha.user_permissions.remove(Permission.objects.get(codename='view_tougshireauthuser'))
        self.assertFalse(usealpha.has_perm('tougshire_auth.view_tougshireauthuser'))

    def test_user_can_get_perm_from_group(self):
        grualpha = TougshireAuthGroup.objects.get(name='grualpha')
        perm_view_user = Permission.objects.get(codename='view_tougshireauthuser')
        grualpha.permissions.add(perm_view_user)
        usealpha = TougshireAuthUser.objects.get(username='usealpha')
        usealpha.groups.add(grualpha)
        self.assertTrue(usealpha.has_perm('tougshire_auth.view_tougshireauthuser'))

    def test_user_loses_perm_after_leaving_group(self):
        grualpha = TougshireAuthGroup.objects.get(name='grualpha')
        usealpha = TougshireAuthUser.objects.get(username='usealpha')
        usealpha.groups.remove(grualpha)
        self.assertFalse(usealpha.has_perm('tougshire_auth.view_tougshireauthuser'))

class TestAdmin(TestCase):
    def test_group_user_are_registered(self):
        for model in [TougshireAuthGroup, TougshireAuthUser]:
            self.assertIs(
                True,
                admin.site.is_registered(model),
                msg=f'"{model.__name__}" is not registered')

    def test_default_group_not_registered(self):
        self.assertFalse(admin.site.is_registered(Group))

    def test_tougshire_user_admin_model_is_useradmin(self):
        self.assertEqual(admin.site._registry[TougshireAuthUser].__str__()[-9:], 'UserAdmin')

    def test_tougshire_group_admin_model_is_groupadmin(self):
        self.assertEqual(admin.site._registry[TougshireAuthGroup].__str__()[-10:], 'GroupAdmin')

class TestUserName(TestCase):
    @classmethod
    def setUpTestData(cls):
        TougshireAuthUser.objects.create(
            username="usealpha",
            first_name="Alpha",
            last_name="User",
            display_name="Alf",
            email="usealpha@tougshire.com"
        )

    def test_name_with_no_setting(self):
        if hasattr(settings, 'AUTH_USER_DISPLAY'):
            delattr(settings, 'AUTH_USER_DISPLAY')
        usealpha = TougshireAuthUser.objects.first()
        self.assertEqual(usealpha.__str__(), 'Alf')

    def test_name_with_empty_setting(self):
        settings.AUTH_USER_DISPLAY = ''
        usealpha = TougshireAuthUser.objects.first()
        self.assertEqual(usealpha.__str__(), 'Alf')

    def test_name_with_bad_setting(self):
        settings.AUTH_USER_DISPLAY = 'bad'
        usealpha = TougshireAuthUser.objects.first()
        self.assertEqual(usealpha.__str__(), 'Alf')

    def test_name_with_name_setting(self):
        settings.AUTH_USER_DISPLAY = 'name'
        usealpha = TougshireAuthUser.objects.first()
        self.assertEqual(usealpha.__str__(), 'Alf')

    def test_name_with_firstname_setting(self):
        settings.AUTH_USER_DISPLAY = 'first_name'
        usealpha = TougshireAuthUser.objects.first()
        self.assertEqual(usealpha.__str__(), 'Alpha')

    def test_name_with_lastname_setting(self):
        settings.AUTH_USER_DISPLAY = 'last_name'
        usealpha = TougshireAuthUser.objects.first()
        self.assertEqual(usealpha.__str__(), 'User')

    def test_name_with_email_setting(self):
        settings.AUTH_USER_DISPLAY = 'email'
        usealpha = TougshireAuthUser.objects.first()
        self.assertEqual(usealpha.__str__(), 'usealpha@tougshire.com')

    def test_first_name_last_name_if_no_display_name(self):
        if hasattr(settings, 'AUTH_USER_DISPLAY'):
            delattr(settings, 'AUTH_USER_DISPLAY')
        usealpha = TougshireAuthUser.objects.first()
        usealpha.display_name = ''
        self.assertEqual(usealpha.__str__(), 'Alpha User')

    def test_stripped_first_name_if_no_display_name(self):
        if hasattr(settings, 'AUTH_USER_DISPLAY'):
            delattr(settings, 'AUTH_USER_DISPLAY')
        usealpha = TougshireAuthUser.objects.first()
        usealpha.display_name = ''
        usealpha.last_name = ''
        self.assertEqual(usealpha.__str__(), 'Alpha')
