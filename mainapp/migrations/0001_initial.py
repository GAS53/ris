# Generated by Django 4.0.6 on 2022-07-20 19:24

from django.db import migrations, models
import django.db.models.deletion
import mainapp.models.Images


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Base_bad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bad_type', models.CharField(default='ленточный', editable=False, max_length=20, verbose_name='Тип фундамента')),
            ],
        ),
        migrations.CreateModel(
            name='Base_matherials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matherials_type', models.CharField(default='кирпич', editable=False, max_length=20, verbose_name='Тип постройки')),
            ],
        ),
        migrations.CreateModel(
            name='Base_work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_type', models.CharField(default='подготовительные', editable=False, max_length=20, verbose_name='Вид работ')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создана')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Корректирована')),
                ('deleted', models.BooleanField(default=False, verbose_name='удалена(помечена удаленной)')),
                ('title', models.CharField(max_length=128, verbose_name='Заголовок')),
                ('preamble', models.CharField(max_length=512, verbose_name='Вступление')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Основной текст')),
                ('picture', models.ImageField(blank=True, max_length=255, null=True, upload_to='image_news/%Y/%m/%d/', verbose_name='картинка к новости')),
            ],
            options={
                'verbose_name': 'Новости',
                'verbose_name_plural': 'Новости',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создана')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Корректирована')),
                ('deleted', models.BooleanField(default=False, verbose_name='удалена(помечена удаленной)')),
                ('title', models.CharField(default='Null', max_length=100, verbose_name='Заголовок')),
                ('body', models.CharField(default='Null', max_length=1000, verbose_name='Описание проекта')),
                ('map', models.CharField(default='Null', max_length=1000, verbose_name='Расположение объекта(вставляем после  src="..."')),
                ('start_date', models.DateField(verbose_name='Дата начала строительства')),
                ('stop_date', models.DateField(blank=True, null=True, verbose_name='Дата окончания строительства')),
                ('house_area', models.PositiveSmallIntegerField(verbose_name='Площадь дома')),
                ('bad', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.base_bad')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.base_matherials')),
                ('works', models.ManyToManyField(to='mainapp.base_work')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создана')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Корректирована')),
                ('deleted', models.BooleanField(default=False, verbose_name='удалена(помечена удаленной)')),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to=mainapp.models.Images.user_directory_path, verbose_name='Фото проектов')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.project')),
                ('works', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.base_work')),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фотографии',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='FeedabckModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создана')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Корректирована')),
                ('deleted', models.BooleanField(default=False, verbose_name='удалена(помечена удаленной)')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('body', models.TextField(verbose_name='Отзыв')),
                ('name_feetbacker', models.CharField(max_length=55, verbose_name='Имя написавшего отзыв')),
                ('photo_feetbacker', models.ImageField(blank=True, null=True, upload_to='images/feedbackers', verbose_name='Фото написавшего отзыв')),
                ('bad', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.base_bad')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.base_matherials')),
                ('project', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.project')),
                ('works', models.ManyToManyField(to='mainapp.base_work')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'ordering': ('-created',),
            },
        ),
    ]
