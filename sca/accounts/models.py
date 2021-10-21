from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from sca.core.models import TimeStampedModel
from .managers import CustomUserManager


# Create your models here.
class User(TimeStampedModel, AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField('email address', unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def get_full_name(self):
        return f'{self.last_name} {self.first_name}'

    def enroll(self, course):
        self.courses.add(course)

    def is_enrolled(self, course_id):
        return self.courses.filter(pk=course_id).exists()

    

    def __str__(self):
        return self.email
