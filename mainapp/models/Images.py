from hmac import trans_36
from django.db import models
from django.utils.translation import gettext_lazy as gl
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from .Project import Project
from mainapp.models import Base
from transliterate import slugify



def user_directory_path(instance, filename):
    date = str(instance.project.start_date).split(' ')[0]
    name = slugify(instance.project.title)
    return f'media/photo_projects/{date}_{name}/{filename}'



class Image(Base.SuperBase):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Объект')
    works = models.ForeignKey(Base.Base_work, on_delete=models.DO_NOTHING, verbose_name='Тип работы на фото', db_column='works' )
    describe = models.CharField(verbose_name='Подпись к картинке', max_length=100, blank=True, null=True)
    
    image = models.ImageField(max_length=255, verbose_name='Фото объекта', blank=True, null=True, upload_to=user_directory_path)
    mini_thumbnail_wm = ImageSpecField(source='image',
        processors=[ResizeToFill(200, 250)],
        options={'quality': 60})
    main_thumbnail_wm = ImageSpecField(source='image',
        processors=[ResizeToFill(640, 480)])

    class Meta:
        verbose_name = gl("Фотография к проекту")
        verbose_name_plural = gl("Фотографии к проектам")
        ordering = ("-created",)

    def __str__(self):
        return f'id {self.pk} project {self.project}'