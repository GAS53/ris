from django.db import models
from .Project import Project
from mainapp.models import Base
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class FeedabckModel(Base.SuperBase):
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    body = models.TextField(verbose_name='Отзыв')
    name_feetbacker = models.CharField(verbose_name='Имя написавшего отзыв', max_length=55)
    photo_feetbacker = models.ImageField(verbose_name='Фото написавшего отзыв', blank=True, null=True, upload_to='images/feedbackers')
    mini_thumbnail_wm = ImageSpecField(source='image',
        processors=[ResizeToFill(200, 250)],
        options={'quality': 60})
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING, default=None, verbose_name='Название объекта')
    bad = models.ForeignKey(Base.Base_bad, on_delete=models.DO_NOTHING, verbose_name='Тип фундамента')
    material = models.ForeignKey(Base.Base_matherials, on_delete=models.DO_NOTHING, verbose_name='Основной материал стен')
    works = models.ManyToManyField(Base.Base_work, verbose_name='Работы выполненные на обьекте')
        
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ("-created",)