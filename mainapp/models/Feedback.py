from django.db import models
from django.utils.translation import gettext_lazy as gl
from .Project import Project


class FeedabckModel(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    body = models.CharField(verbose_name='Отзыв', max_length=1000)
    name = models.CharField(verbose_name='Имя написавшего отзыв', max_length=55)
    photo_feetbacker = models.ImageField(verbose_name='Фото написавшего отзыв', blank=True, null=True, upload_to='images/feedbackers')
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    deleted = models.BooleanField(default=False, verbose_name='удалена(помечена удаленной)')
    
    class Meta:
        verbose_name = gl("Отзыв")
        verbose_name_plural = gl("Отзывы")
        # ordering = ("-created",)