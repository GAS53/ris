from django.db import models
from django.utils.translation import gettext_lazy as gl

from mainapp.models.Base import Base_work, Base_matherials




class Projects(Base_matherials):
    name = models.CharField(verbose_name='Имя проекта', max_length=25)
    mini_description = models.CharField(verbose_name='Описание проекта', max_length=100)
    full_description = models.CharField(verbose_name='Описание проекта', max_length=1000)
    map_mark = models.CharField(default='Владелец не захотел указывть расположение обьекта', verbose_name='Расположене объекта', max_length=150)
    


class Images(Base_work):
    path = models.ImageField(max_length=255, verbose_name='Фото проектов', blank=True, null=True, upload_to='images/projects'))
    project_id = models.ManyToManyField(Projects, on_delete=models.DO_NOTHING)
    
