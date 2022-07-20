from django.contrib import admin
from .models import News, Images, Project
from django.contrib.auth.models import Group

admin.site.unregister(Group)

@admin.register(News.News)
class NewsAdmin(admin.ModelAdmin):
    # list_display = ['created', 'title', 'preamble', 'picture', 'updated', 'deleted' ]
    # ordering = ['title', 'preamble']
    # list_per_page = 10
    # list_filter = ['created', 'updated', 'deleted' ]
    # search_fields = ['title', 'preamble', 'body']
    # actions = ['mark_deleted']

    def mark_deleted(self):
        self.deleted = True
        self.save()

@admin.register(Images.Image)
class ImagesAdmin(admin.ModelAdmin):
    # list_display = ['project', 'works', 'image', 'deleted']
    # ordering = ['image']
    # list_per_page = 10
    # list_filter = ['deleted']
    # search_fields = ['image']
    # actions = ['mark_deleted']

    def mark_deleted(self, request, *kwargs):
        self.deleted = True
        self.save()
    

@admin.register(Project.Project)
class ProjectAdmin(admin.ModelAdmin):
    # list_display = [ 'title', 'map', 'deleted']
    # ordering = [ 'title']
    # list_per_page = 10
    # list_filter = [ 'created', 'deleted' ]
    # search_fields = ['title', 'body']
    # actions = ['mark_deleted']

    def mark_deleted(self):
        self.deleted = True
        self.save()

# admin.site.register(User)