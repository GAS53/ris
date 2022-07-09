from django.db import models
from django.utils.translation import gettext_lazy as gl

class Base_work(models.Model):
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
    
    rubric = models.SmallIntegerField(choices=works, default=PRE, verbose_name='Вид работ')
    

    class Meta:
        abstract = True
        

class Base_matherials(models.Model):
    BRICK = 'br'  # кирпич
    BLOCKS = 'bl'
    FRAME = 'fr'  # каркас
    matherials = [
        (BRICK, 'Кирпич'),
        (BLOCKS, 'Блоки'),
        (FRAME, 'Каркас'),
    ]
    name = models.CharField(verbose_name='Тип постройки', max_length=2, choices=matherials, default=BRICK)
    
    class Meta:
        abstract = True