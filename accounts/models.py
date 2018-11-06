from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, _user_has_perm
)
from django.core import validators
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from collections import OrderedDict


class AccountManager(BaseUserManager):
    def create_user(self, request_data, **kwargs):
        now = timezone.now()
        if not request_data['user_name']:
            raise ValueError('Users must have an username.')

        if not request_data['email']:
            raise ValueError('Users must have an email address.')

        if not request_data['password']:
            raise ValueError('Users must have an password.')

        user = self.model(
            user_name=request_data['user_name'],
            email=self.normalize_email(request_data['email']),
            password=request_data['password'],
            last_login=now
        )

        user.set_password(request_data['password'])
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=30, unique=True)
    email = models.TextField()
    password = models.TextField()
    last_login = models.DateTimeField()

    objects = AccountManager()

    USERNAME_FIELD = 'user_name'
    # REQUIRED_FIELDS = []

    def to_dict(self):
        add = (("user_id", self.user_id),
               ("user_name", self.user_name),
               ("email", self.email),
               ("password", self.password),
               ("last_login", self.last_login))

        return OrderedDict(add)

    class Meta:
        managed = False
        db_table = 'account'
        swappable = 'AUTH_USER_MODEL'
