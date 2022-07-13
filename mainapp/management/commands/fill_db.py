from django.core.management import BaseCommand
from mainapp.models import News, Images, Project
from random import choice
import string
import datetime


def get_text(num):
    res = ''
    for i in range(num):
        res += choice(string.ascii_letters)
    return res




class Command(BaseCommand):
    help = ('заполнение новостями list_news')

    def handle(self, *args, **options):
        count = 10
        print(f'старт заполнения произвольными новостями')
        li = []
        for _ in range(count):
            li.append(
            News.News(
                title = get_text(5),
                preamble = get_text(25),
                body = get_text(100),


                
            ))
        
        News.News.objects.bulk_create(li)
        print(f'окончание заполнения {count} новостями')
        li.clear()

        for _ in range(count):
            li.append(Project.Project(
                # name = get_text(5),
                mini_description = get_text(20),
                full_description = get_text(250),
                map_mark = "https://yandex.ru/maps/org/petropavlovskaya_krepost/146720535721/?utm_medium=mapframe&utm_source=maps",
                start_date = datetime.datetime.now(),
                stop_date = datetime.datetime.now(),
                house_type = choice(['br', 'bl', 'fr']),
            ))
        Project.Project.objects.bulk_create(li)
        print(f'закончено добавление проектов')
        li.clear()
        pictures = count+20
        projects = []
        for num in Project.Project.objects.all():
            projects.append(num)

        for _ in range(pictures):
            li.append(Images.Image(
                # name = get_text(5),
                path = get_text(5),
                created = datetime.datetime.now(),
                project = choice(projects),
                work_type = choice(['ge', 'pr', 'ea', 'st', 'co', 'fi', 'he', 'fi','is', 'lo'])



            ))
        Images.Image.objects.bulk_create(li)
        print(f'закончено добавление {pictures} картинок')
        li.clear()
       

        
        






