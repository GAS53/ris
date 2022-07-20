from django.db import models
from .Project import Project
from mainapp.models import Base


class FeedabckModel(Base.SuperBase):
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    body = models.TextField(verbose_name='Отзыв')
    name_feetbacker = models.CharField(verbose_name='Имя написавшего отзыв', max_length=55)
    photo_feetbacker = models.ImageField(verbose_name='Фото написавшего отзыв', blank=True, null=True, upload_to='images/feedbackers')
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING, default=None)
    bad = models.ForeignKey(Base.Base_bad, on_delete=models.DO_NOTHING)
    material = models.ForeignKey(Base.Base_matherials, on_delete=models.DO_NOTHING)
    works = models.ManyToManyField(Base.Base_work)
        
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ("-created",)