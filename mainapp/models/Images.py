from hmac import trans_36
from django.db import models
from django.utils.translation import gettext_lazy as gl
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from .Project import Project
from mainapp.models.Base import Base_work
# from mainapp.processors import WatermarkOverlay
import cyrtranslit
from config import settings 

def user_directory_path(instance, filename):
    return f"photo_projects/{cyrtranslit.to_latin(instance.project.mini_description, 'ru')}_{instance.project.start_date}/{filename}"


class Image(Base_work):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(max_length=255, verbose_name='Фото проектов', blank=True, null=True, upload_to=user_directory_path)
    mini_thumbnail_wm = ImageSpecField(source='image',
      processors=[ResizeToFill(200, 250),
      # WatermarkOverlay(),
        ],
        #   format='JPEG',
        options={'quality': 60})
    main_thumbnail_wm = ImageSpecField(source='image',
        processors=[ResizeToFill(1920, 1080),
        # WatermarkOverlay(),
        ],
        #   format='JPEG',
        )


    






    class Meta:
        verbose_name = gl("Фото")
        verbose_name_plural = gl("Фотографии")
        ordering = ("-created",)

    def __str__(self) -> str:
        return f'id {self.pk} project {self.project}'