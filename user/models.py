from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
    # id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    # password = models.CharField(max_length=128, verbose_name='password')
    # last_login = models.DateTimeField(blank=True, null=True, verbose_name='last login')
    # is_superuser = models.BooleanField(default=False,
    #                                      help_text='Designates that this user has all permissions without explicitly assigning them.',
    #                                      verbose_name='superuser status')
    # username = models.CharField(error_messages={'unique': 'A user with that username already exists.'},
    #                               help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
    #                               max_length=150, unique=True,
    #                               validators=[UnicodeUsernameValidator()],
    #                               verbose_name='username')
    # first_name = models.CharField(blank=True, max_length=30, verbose_name='first name')
    # last_name = models.CharField(blank=True, max_length=150, verbose_name='last name')
    # email = models.EmailField(blank=True, max_length=254, verbose_name='email address')
    # is_staff = models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.',
    #                      verbose_name='staff status')
    # is_active = models.BooleanField(default=True,
    #                                   help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.',
    #                                   verbose_name='active')
    # date_joined = models.DateTimeField(default=now, verbose_name='date joined')
    #
    # REQUIRED_FIELDS = []
    # USERNAME_FIELD = 'username'
    # is_anonymous = False
    # is_authenticated = True


