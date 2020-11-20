from django.db import models
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
import datetime
from django.core.validators import RegexValidator


class CustomUserManager(BaseUserManager):

    def _create_user(self, phone_number, password, **extra_fields):
        now = timezone.now()
        if not phone_number:
            raise ValueError('The given phone_number must be set')
        user = self.model(phone_number=phone_number, is_active=True, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, password=None, is_provider=None, **extra_fields):
        return self._create_user(phone_number, password, **extra_fields)

    def create_superuser(self, phone_number, password=None, **extra_fields):
        user = self._create_user(phone_number, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number is error")
    phone_number = models.CharField(validators=[phone_regex], max_length=14, unique=True)
    is_director = models.BooleanField(default=False)
    is_accountant = models.BooleanField(default=False)
    is_warehouseman = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_chief_technological_man = models.BooleanField(default=False)
    is_chief_specialist = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()