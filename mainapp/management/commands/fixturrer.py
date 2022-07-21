from django.core.management import BaseCommand, call_command, execute_from_command_line
from datetime import datetime
import os
import argparse

def strip_date(last_time):
    last_time = str(last_time)
    last_time = last_time.replace(' ', '_')
    last_time = last_time[:16]
    last_time += '.json'
    return last_time

def get_last_fixture():
    path = 'fixtures/'
    last_time = None
    files = os.listdir(path)
    for file_name in files:
        stat_file = os.stat(f'{path}{file_name}')
        date_file = stat_file.st_ctime
        if last_time == None:
            last_time=date_file
        elif last_time < date_file:
            last_time = date_file
    if last_time == None:
        raise ValueError('не найден последний файл')
    for file_name in files:
        stat_file = os.stat(f'{path}{file_name}')
        if stat_file.st_ctime == last_time:
            print(f'Загружаю последний дамп {file_name}')
            return f'fixtures/{file_name}'
        else:
            print('неведомая ошибка')


def get_name_fixture():
    return f'fixtures/full*{strip_date(datetime.now())}'

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('action', type=str)
        return super().add_arguments(parser)

    def handle(self, *args, **options):
        res = options['action']
        print(f'Действие {res} fixtures')
        if 'load' == res:
            call_command('loaddata', get_last_fixture())
        elif 'dump'== res:
            call_command('dumpdata', '-o', get_name_fixture())
        else:
            print(f'Неверно введена команда {res} должно быть load или dump')