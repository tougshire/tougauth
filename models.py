from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _

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

    def get_display_name(self):
        if self.display_name > '':
            return self.display_name
        elif self.first_name + self.last_name > '':
            return f'{self.first_name} {self.last_name}'
        else:
            return self.username

    get_display_name.short_description = 'name'
