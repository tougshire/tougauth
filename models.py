from django.contrib.auth.models import AbstractUser, Group as ContribGroup

class User(AbstractUser):
    pass

class Group(ContribGroup):
    pass
