from django.core.management import BaseCommand
from mainapp.models import News
from random import choice
import string

def get_text(num):
    res = ''
    for i in range(num):
        res += choice(string.ascii_letters)
    return res




class Command(BaseCommand):
    help = ('заполнение новостями list_news')

    def handle(self, *args, **options):
        count_news = 10
        print(f'старт заполнения произвольными новостями')
        li_news = []
        for i in range(count_news):
            li_news.append(
            News(
                title = get_text(5),
                rubric = 2,
                preamble = get_text(25),
                body = get_text(100),
            ))
        
        News.objects.bulk_create(li_news)