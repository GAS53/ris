from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from mainapp.models.Base import SuperBase



class News(SuperBase):
    title = models.CharField(max_length=128, verbose_name='Заголовок')
    preamble = models.CharField(max_length=512, verbose_name='Вступление')
    body = models.TextField(blank=True, null=True, verbose_name="Основной текст")

    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"
        ordering = ("-created",)
    
    def __str__(self):
        return f"{self.pk} {self.title}"



class NewsPicture(SuperBase):
    picture = models.ImageField(max_length=255, verbose_name='картинка к новости', blank=True, null=True, upload_to='media/image_news/%Y/%m/%d/')
    mini_thumbnail_wm = ImageSpecField(source='picture', processors=[ResizeToFill(200, 250)])
    main_thumbnail_wm = ImageSpecField(source='picture', processors=[ResizeToFill(1920, 1080)])
    describe = models.CharField(verbose_name='Подпись к картинке', max_length=100, blank=True, null=True)
    news = models.ForeignKey(News, verbose_name='К какой новости относиться картинка', on_delete=models.CASCADE)


    class Meta:
        verbose_name = "Картинка к новости"
        verbose_name_plural = "Картинки к новости"
        ordering = ("-created",)
    
    def __str__(self):
        return f"{self.pk} {self.describe}"