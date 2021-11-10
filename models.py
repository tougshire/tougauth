from django.core.exceptions import FieldDoesNotExist
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class TougshireAuthGroup(Group):
    class Meta:
        app_label = 'tougshire_auth'
        verbose_name = 'group'

class TougshireAuthUser(AbstractUser):
    display_name = models.CharField(
        'display_name',
        max_length=50,
        blank=True,
        help_text='A display name, or nickname, for example something that would follow "Hello, "'
    )

    @property
    def name(self):
        if self.display_name > '':
            return self.display_name
        elif self.first_name + self.last_name > '':
            return f'{self.first_name} {self.last_name}'.strip()
        else:
            return self.username

    def __str__(self):
        if hasattr(settings, 'AUTH_USER_DISPLAY'):
            if settings.AUTH_USER_DISPLAY > '':
                try:
                    return getattr(self, settings.AUTH_USER_DISPLAY)
                except AttributeError:
                    print('Attribute error in TougshireAuthUser __str__')
                    pass

        return self.name
