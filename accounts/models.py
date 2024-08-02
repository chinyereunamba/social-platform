from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('All users must have an email address')
        if not username:
            raise ValueError('All users must have a username')

        email = self.normalize_email(email=email).lower()

        user = self.model(
            email=email,
            username=username,
            **extra_fields
        )

        user.save(using=self._db)
        user.set_password(password)

        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        user = self.create_user(
            email=email,
            password=password,
            username=username,
            **extra_fields
        )

        user.save(using=self._db)

        return user


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("Email"), max_length=80, unique=True)
    username = models.CharField(_("Username"), max_length=80, unique=True)

    first_name = models.CharField(_("First Name"), max_length=80, blank=True)
    last_name = models.CharField(_("Last Name"), max_length=80, blank=True)

    bio = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='img/', blank=True)

    date_joined = models.DateField(auto_created=True, blank=True)
    last_login = models.DateTimeField(auto_now=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label: str) -> bool:
        return True
    
