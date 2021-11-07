from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _

class SuvapuliGroup(Group):
    class Meta:
        app_label = 'suvapuli_app'
        verbose_name = 'group'

class SuvapuliUser(AbstractUser):
    display_name = models.CharField(
        'display name',
        max_length=50,
        blank=True,
        help_text='A display name, or nickname, if different from firstname lastname'
    )

    def __str__(self):
        if self.display_name > '':
            return self.display_name
        elif(self.first_name + self.last_name > ''):
            return f'{self.first_name} {self.last_name}'
        else:
            return self.username
