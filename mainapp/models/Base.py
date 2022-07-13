from django.db import models
from django.utils.translation import gettext_lazy as gl

class BaseManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)

    def delete(self, *args):
        self.deleted = True
        self.save()

class SuperBase(models.Model):
    objects = BaseManager()
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создана", editable=False)
    deleted = models.BooleanField(default=False, verbose_name='удалена(помечена удаленной)')

    class Meta:
        abstract = True

    def delete(self, *args):
        self.deleted = True
        self.save()
  

class Base_work(SuperBase):
    GEO = 'ge'
    PRE = 'pr'
    EAR = 'ea'
    STONY = 'st'
    CONCRETE = 'co'
    FITTER = 'fi'
    HEALING = 'he'
    FINISHING = 'fi'
    ISOLATIG = 'is'
    LOW_POWER = 'lo'
    works = [
        (GEO, 'Геодезические'),
        (PRE, 'Подготовительные'),
        (EAR, 'Земляные'),
        (STONY, 'Каменные'),
        (CONCRETE, 'Бетонные/железобетонные'),
        (FITTER, 'Монтажные'),
        (HEALING, 'Кровельные'),
        (FINISHING, 'Отделочные'),
        (ISOLATIG, 'Изоляционные'),
        (LOW_POWER, 'Слаботочные'),
    ]
    
    work_type = models.CharField(verbose_name='Вид работ', max_length=2 ,choices=works, default=PRE)
    

    class Meta:
        abstract = True
        

class Base_matherials(SuperBase):
    BRICK = 'br'  # кирпич
    BLOCKS = 'bl'
    FRAME = 'fr'  # каркас
    matherials = [
        (BRICK, 'Кирпич'),
        (BLOCKS, 'Блоки'),
        (FRAME, 'Каркас'),
    ]
    house_type = models.CharField(verbose_name='Тип постройки', max_length=2, choices=matherials, default=BRICK)
    
    class Meta:
        abstract = True