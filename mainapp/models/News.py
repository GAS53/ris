from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill



from mainapp.models.Base import SuperBase



class News(SuperBase):
    title = models.CharField(max_length=128, verbose_name='Заголовок')
    preamble = models.CharField(max_length=512, verbose_name='Вступление')
    body = models.TextField(blank=True, null=True, verbose_name="Основной текст")

    picture = models.ImageField(max_length=255, verbose_name='картинка к новости', blank=True, null=True, upload_to='image_news/%Y/%m/%d/')
    mini_thumbnail_wm = ImageSpecField(source='picture', processors=[ResizeToFill(200, 250)])
    main_thumbnail_wm = ImageSpecField(source='picture', processors=[ResizeToFill(1920, 1080)])                                  


    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"
        ordering = ("-created",)
    
    def __str__(self):
        return f"{self.pk} {self.title}"


