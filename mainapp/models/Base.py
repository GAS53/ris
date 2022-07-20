from django.db import models

class BaseManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)

    def delete(self, *args):
        self.deleted = True
        self.save()




class SuperBase(models.Model):
    objects = BaseManager()
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создана", editable=False)
    updated = models.DateTimeField(auto_now=True, verbose_name="Корректирована")
    deleted = models.BooleanField(default=False, verbose_name='удалена(помечена удаленной)')

    class Meta:
        abstract = True

    def delete(self, *args):
        self.deleted = True
        self.save()
  

class Base_work(models.Model):
    work_type = models.CharField(editable=False, verbose_name='Вид работ', max_length=20, default='подготовительные')

class Base_matherials(models.Model):
    matherials_type = models.CharField(editable=False, verbose_name='Тип постройки', max_length=20, default='кирпич')

class Base_bad(models.Model):
    bad_type = models.CharField(editable=False, verbose_name='Тип фундамента', max_length=20, default='ленточный')

