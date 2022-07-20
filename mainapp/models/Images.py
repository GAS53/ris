from hmac import trans_36
from django.db import models
from django.utils.translation import gettext_lazy as gl
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from .Project import Project
from mainapp.models import Base


def user_directory_path(self):
    return f'images/projects/{self.project.created}_{self.project.title}/'



class Image(Base.SuperBase):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    works = models.ForeignKey(Base.Base_work, on_delete=models.DO_NOTHING)
    
    image = models.ImageField(max_length=255, verbose_name='Фото проектов', blank=True, null=True, upload_to=user_directory_path)
    mini_thumbnail_wm = ImageSpecField(source='image',
      processors=[ResizeToFill(200, 250)],
        options={'quality': 60})
    main_thumbnail_wm = ImageSpecField(source='image')

    class Meta:
        verbose_name = gl("Фото")
        verbose_name_plural = gl("Фотографии")
        ordering = ("-created",)

    def __str__(self):
        return f'id {self.pk} project {self.project}'