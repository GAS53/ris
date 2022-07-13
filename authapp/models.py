from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # username = models.CharField(verbose_name='Имя пользователя', max_length=35)
    

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        # USERNAME_FIELD = username