from django.db import models
from django.utils.translation import gettext_lazy as gl

from mainapp.models.Base import Base_work

class NewsManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class News(Base_work):
    objects = NewsManager()
    title = models.CharField(max_length=128, verbose_name='Заголовок')
    
    preamble = models.CharField(max_length=512, verbose_name='Вступление')
    body = models.TextField(blank=True, null=True, verbose_name="Основной текст")


    picture = models.ImageField(max_length=255, verbose_name='картинка к новости', blank=True, null=True, upload_to='images/')

    created = models.DateTimeField(auto_now_add=True, verbose_name="Создана", editable=False)
    updated = models.DateTimeField(auto_now=True, verbose_name="Корректирована", editable=False)
    deleted = models.BooleanField(default=False, verbose_name='удалена(помечена удаленной)')


    class Meta:
        verbose_name = gl("Новости")
        verbose_name_plural = gl("Новости")
        ordering = ("-created",)
    
    def __str__(self):
        return f"{self.pk} {self.title}"

    def delete(self, *args):
        self.deleted = True
        self.save()
