from django.contrib.auth.models import AbstractUser
from django.db import models
from reporting_portal_auth.constants.enums import Role


class User(AbstractUser):
    role = Role.get_list_of_tuples()

    name = models.CharField(max_length=20)
    phone_no = models.IntegerField(null=True)
    user_role = models.CharField(max_length=20, choices=role)
    profile_pic = models.CharField(max_length=50)
