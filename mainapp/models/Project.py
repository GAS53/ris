from django.db import models
from django.utils.translation import gettext_lazy as gl

from mainapp.models import Base


class Project(Base.SuperBase):
    title = models.CharField(verbose_name='Заголовок', max_length=100, default='Null')
    body = models.CharField(verbose_name='Описание проекта', max_length=1000, default='Null')
    map = models.CharField(default='Null', verbose_name='Расположение объекта(вставляем после  src="..."', max_length=1000)
    start_date = models.DateField(verbose_name="Дата начала строительства")
    stop_date = models.DateField(verbose_name="Дата окончания строительства", blank=True, null=True)
    house_area = models.PositiveSmallIntegerField(verbose_name='Площадь дома')

    works = models.ManyToManyField(Base.Base_work, verbose_name='Типы выполненных работ')
    material = models.ForeignKey(Base.Base_matherials, on_delete=models.DO_NOTHING, verbose_name='Основной материал стен')
    bad = models.ForeignKey(Base.Base_bad, on_delete=models.DO_NOTHING, verbose_name='Тип фундамента')



    class Meta:
        verbose_name = gl("Проект")
        verbose_name_plural = gl("Проекты")
        ordering = ("-created",)


    def __str__(self) -> str:
        return f'{self.pk} {self.title}'