from django.db import models
from django.utils.translation import gettext_lazy as gl

from .Project import Project
from mainapp.models.Base import Base_work



class Image(Base_work):
    path = models.ImageField(max_length=255, verbose_name='Фото проектов', blank=True, null=True, upload_to='images/projects')
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    
    class Meta:
        verbose_name = gl("Фото")
        verbose_name_plural = gl("Фотографии")
        ordering = ("-created",)

    def __str__(self) -> str:
        return f'id {self.pk} project {self.project}'