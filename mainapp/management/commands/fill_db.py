from django.core.management import BaseCommand, call_command
from mainapp.models import Base, News
import time
from transliterate.contrib.apps.translipsum import TranslipsumGenerator

def timit(title):
    def in_wrapp(func):
        def wrapper(*num):
            print(f'Начало работы функция заполнене типами {title}')
            start = time.time()
            res = func(*num)
            stop = time.time()
            print(f'Конец работы функции заполнене типами {title} время работы {round((stop-start), 3)} сек')
            return res
        return wrapper
    return in_wrapp


@timit('работ')
def fill_base_works():
    works = ['не выбран', 'Геодезические', 'Подготовительные', 'Земляные', 'Каменные', 'Бетонные/железобетонные', 'Монтажные',
             'Кровельные', 'Отделочные', 'Изоляционные', 'Слаботочные']
    li = []
    for work in works:
        li.append(Base.Base_work(work_type=work))
    Base.Base_work.objects.all().delete()
    Base.Base_work.objects.bulk_create(li)


@timit('материалов')
def fill_base_materials():
    materials = ['не выбран', 'Кирпич', 'Блоки', 'Каркас']
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


def create_superuser(user):
    call_command('createsuperuser', '--username', f'{user}', '--email', 'test@test.ru')
    print(f'создан супуер пользователь {user}')

@timit('новостей')
def fill_news(quantity):
    li = []
    for _ in range(quantity):
        generator = TranslipsumGenerator(language_code='ru')
        li.append(News.News(title=generator.generate_paragraph(), preamble=generator.generate_paragraph(), body=generator.generate_paragraph()))
    News.News.objects.all().delete()
    News.News.objects.bulk_create(li)



class Command(BaseCommand):

    def handle(self, *args, **options):
        fill_base_works()
        fill_base_materials()
        # fill_base_bad()
        # fill_news(20)
        # create_superuser('test')



        
        






