# Generated by Django 4.0.6 on 2022-07-23 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emailer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('name', models.CharField(max_length=70)),
                ('question', models.CharField(max_length=1000, verbose_name='Сообщение')),
            ],
        ),
        migrations.AlterField(
            model_name='newspicture',
            name='picture',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='media/image_news/%Y/%m/%d/', verbose_name='картинка к новости'),
        ),
    ]
