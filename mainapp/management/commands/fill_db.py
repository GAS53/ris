from django.core.management import BaseCommand
from mainapp.models import Base
import time

def timit(title):
    def in_wrapp(func):
        def wrapper(*num):
            print(f'Начало работы функция заполнене типами {title}')
            start = time.time()
            res = func(*num)
            stop = time.time()
            print(f'Конец работы функции заполнене типами {title} время работы {stop-start} сек')
            return res
        return wrapper
    return in_wrapp


@timit('работ')
def fill_base_works():
    works = ['Геодезические', 'Подготовительные', 'Земляные', 'Каменные', 'Бетонные/железобетонные', 'Монтажные',
             'Кровельные', 'Отделочные', 'Изоляционные', 'Слаботочные']
    li = []
    for work in works:
        li.append(Base.Base_work(work_type=work))
    Base.Base_work.objects.all().delete()
    Base.Base_work.objects.bulk_create(li)


@timit('материалов')
def fill_base_materials():
    materials = ['Кирпич', 'Блоки', 'Каркас']
    li = []
    for mat in materials:
        li.append(Base.Base_matherials(matherials_type=mat))
    Base.Base_matherials.objects.all().delete()
    Base.Base_matherials.objects.bulk_create(li)

@timit('фундаментов')
def fill_base_bad():
    bads = ['ленточный', 'столбчатый', 'свайный', 'плитный', 'комбинированный']
    li = []
    for bad in bads:
        li.append(Base.Base_bad(bad_type=bad))
    Base.Base_bad.objects.all().delete()
    Base.Base_bad.objects.bulk_create(li)


class Command(BaseCommand):

    def handle(self, *args, **options):
        fill_base_works()
        fill_base_materials()
        fill_base_bad()



        
        






