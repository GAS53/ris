from django.db import models


class Emailer(models.Model):
    email = models.EmailField(verbose_name='Email')
    name = models.CharField(max_length=70)
    question = models.CharField(verbose_name='Сообщение', max_length=1000)
