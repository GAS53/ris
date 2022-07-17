from django.db import models
from django.utils.translation import gettext_lazy as gl

from mainapp.models.Base import Base_matherials



class Project(Base_matherials):
    mini_description = models.CharField(verbose_name='Краткое описание', max_length=100)
    full_description = models.CharField(verbose_name='Полное описание проекта', max_length=1000)
    map_mark = models.CharField(default='Владелец не захотел указывть расположение обьекта', verbose_name='Расположение объекта', max_length=150)
    start_date = models.DateField(verbose_name="Дата начала строительства")
    stop_date = models.DateField(verbose_name="Дата окончания строительства", blank=True, null=True)
    

    class Meta:
        verbose_name = gl("Проект")
        verbose_name_plural = gl("Проекты")
        ordering = ("-created",)


    def __str__(self) -> str:
        return f'{self.pk} {self.mini_description}'