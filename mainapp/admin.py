from django.contrib import admin
from .models import News, Images
from authapp.models import User


@admin.register(News.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'preamble', 'body', 'picture', 'created', 'updated', 'deleted' ]
    ordering = ['title', 'preamble']
    list_per_page = 10
    list_filter = ['created', 'updated', 'deleted' ]
    search_fields = ['title', 'preamble', 'body']
    actions = ['mark_deleted']

    def mark_deleted(self):
        self.deleted = True
        self.save()

@admin.register(Images.Image)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['path', 'deleted']
    ordering = ['path']
    list_per_page = 10
    list_filter = ['deleted']
    search_fields = ['path']
    actions = ['mark_deleted']

    def mark_deleted(self, request, *kwargs):
        self.deleted = True
        self.save()
    

@admin.register(Images.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = [ 'mini_description', 'map_mark', 'deleted']
    ordering = [ 'mini_description']
    list_per_page = 10
    list_filter = [ 'created', 'deleted' ]
    search_fields = ['title', 'mini_description', 'full_description']
    actions = ['mark_deleted']

    def mark_deleted(self):
        self.deleted = True
        self.save()

admin.site.register(User)