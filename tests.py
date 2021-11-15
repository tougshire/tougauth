from .models import SuvapuliAuthGroup, SuvapuliAuthUser
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from django.shortcuts import get_object_or_404
from django.test import Client, TestCase
from .urls import urlpatterns
from django.urls import path

class TestUserAndGroup(TestCase):

    @classmethod
    def setUpTestData(cls):
        SuvapuliAuthUser.objects.create(username="usealpha")
        SuvapuliAuthGroup.objects.create(name="grualpha")

    def setUp(self):
        pass

    def test_user_exits(self):
        self.assertEqual(SuvapuliAuthUser.objects.count(), 1)

    def test_user_parameters(self):
        usealpha = SuvapuliAuthUser.objects.get(username='usealpha')
        self.assertEqual(usealpha.__str__(), 'usealpha')

    def test_user_can_have_perm(self):
        usealpha = SuvapuliAuthUser.objects.get(username='usealpha')
        usealpha.user_permissions.add(Permission.objects.get(codename='view_suvapuliauthuser'))
        self.assertTrue(usealpha.has_perm('suvapuli_auth.view_suvapuliauthuser'))

    def test_user_can_lose_perm(self):
        usealpha = SuvapuliAuthUser.objects.get(username='usealpha')
        usealpha.user_permissions.remove(Permission.objects.get(codename='view_suvapuliauthuser'))
        self.assertFalse(usealpha.has_perm('suvapuli_auth.view_suvapuliauthuser'))

    def test_user_can_get_perm_from_group(self):
        grualpha = SuvapuliAuthGroup.objects.get(name='grualpha')
        perm_view_user = Permission.objects.get(codename='view_suvapuliauthuser')
        grualpha.permissions.add(perm_view_user)
        usealpha = SuvapuliAuthUser.objects.get(username='usealpha')
        usealpha.groups.add(grualpha)
        self.assertTrue(usealpha.has_perm('suvapuli_auth.view_suvapuliauthuser'))

    def test_user_loses_perm_after_leaving_group(self):
        grualpha = SuvapuliAuthGroup.objects.get(name='grualpha')
        usealpha = SuvapuliAuthUser.objects.get(username='usealpha')
        usealpha.groups.remove(grualpha)
        self.assertFalse(usealpha.has_perm('suvapuli_auth.view_suvapuliauthuser'))

class TestAdmin(TestCase):
    def test_group_user_are_registered(self):
        for model in [SuvapuliAuthGroup, SuvapuliAuthUser]:
            self.assertIs(
                True,
                admin.site.is_registered(model),
                msg=f'"{model.__name__}" is not registered')

    def test_default_group_not_registered(self):
        self.assertFalse(admin.site.is_registered(Group))

    def test_suvapuli_user_admin_model_is_useradmin(self):
        self.assertEqual(admin.site._registry[SuvapuliAuthUser].__str__()[-9:], 'UserAdmin')

    def test_suvapuli_group_admin_model_is_groupadmin(self):
        self.assertEqual(admin.site._registry[SuvapuliAuthGroup].__str__()[-10:], 'GroupAdmin')

class TestUserName(TestCase):
    @classmethod
    def setUpTestData(cls):
        SuvapuliAuthUser.objects.create(
            username="usealpha",
            first_name="Alpha",
            last_name="User",
            display_name="Alf",
            email="usealpha@suvapuli.com"
        )

    def test_name_with_no_setting(self):
        if hasattr(settings, 'AUTH_USER_DISPLAY'):
            delattr(settings, 'AUTH_USER_DISPLAY')
        usealpha = SuvapuliAuthUser.objects.first()
        self.assertEqual(usealpha.__str__(), 'Alf')

    def test_name_with_empty_setting(self):
        settings.AUTH_USER_DISPLAY = ''
        usealpha = SuvapuliAuthUser.objects.first()
        self.assertEqual(usealpha.__str__(), 'Alf')

    def test_name_with_bad_setting(self):
        settings.AUTH_USER_DISPLAY = 'bad'
        usealpha = SuvapuliAuthUser.objects.first()
        self.assertEqual(usealpha.__str__(), 'Alf')

    def test_name_with_name_setting(self):
        settings.AUTH_USER_DISPLAY = 'name'
        usealpha = SuvapuliAuthUser.objects.first()
        self.assertEqual(usealpha.__str__(), 'Alf')

    def test_name_with_firstname_setting(self):
        settings.AUTH_USER_DISPLAY = 'first_name'
        usealpha = SuvapuliAuthUser.objects.first()
        self.assertEqual(usealpha.__str__(), 'Alpha')

    def test_name_with_lastname_setting(self):
        settings.AUTH_USER_DISPLAY = 'last_name'
        usealpha = SuvapuliAuthUser.objects.first()
        self.assertEqual(usealpha.__str__(), 'User')

    def test_name_with_email_setting(self):
        settings.AUTH_USER_DISPLAY = 'email'
        usealpha = SuvapuliAuthUser.objects.first()
        self.assertEqual(usealpha.__str__(), 'usealpha@suvapuli.com')

    def test_first_name_last_name_if_no_display_name(self):
        if hasattr(settings, 'AUTH_USER_DISPLAY'):
            delattr(settings, 'AUTH_USER_DISPLAY')
        usealpha = SuvapuliAuthUser.objects.first()
        usealpha.display_name = ''
        self.assertEqual(usealpha.__str__(), 'Alpha User')

    def test_stripped_first_name_if_no_display_name(self):
        if hasattr(settings, 'AUTH_USER_DISPLAY'):
            delattr(settings, 'AUTH_USER_DISPLAY')
        usealpha = SuvapuliAuthUser.objects.first()
        usealpha.display_name = ''
        usealpha.last_name = ''
        self.assertEqual(usealpha.__str__(), 'Alpha')

    #test login url.  Comment out if not using
    def test_login_url(self):
        client = Client()
        response = client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)

    def test_bad_login(self):
        SuvapuliAuthUser.objects.create_user(username='admin', password='admin', is_superuser=True)
        client = Client()
        client.post('/accounts/login/', {'username': 'admin', 'password': 'xxxxx'})
        response = client.get('/accounts/profile/')
        template_names = []
        for template in response.templates:
            template_names.append(template.name)
        self.assertNotIn('suvapuli_auth/profile_detail.html', template_names)


    def test_login(self):
        SuvapuliAuthUser.objects.create_user(username='admin', password='admin', is_superuser=True)
        client = Client()
        client.post('/accounts/login/', {'username': 'admin', 'password': 'admin'})
        response = client.get('/accounts/profile/')
        template_names = []
        for template in response.templates:
            template_names.append(template.name)
        self.assertIn('suvapuli_auth/profile_detail.html', template_names)
