from .models import TougshireAuthGroup, TougshireAuthUser
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

