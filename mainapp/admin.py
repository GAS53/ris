from django.contrib import admin
from mainapp.models import News, Images, Project, Feedback
from django.contrib.auth.models import Group, User

# admin.site.unregister(User)
admin.site.unregister(Group)



@admin.register(Feedback.FeedabckModel)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['name_feetbacker', 'project', 'bad', 'material' ]
    ordering = ['title']
    list_per_page = 10
    list_filter = ['title', 'name_feetbacker', 'project', 'bad', 'material', 'created', 'updated', 'deleted' ]
    search_fields = ['title', 'body', 'photo_feetbacker', 'project',]
    actions = ['mark_deleted']




@admin.register(Images.Image)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['project', 'describe', 'image', 'deleted', 'created']
    ordering = ['project']
    list_per_page = 10
    list_filter = ['deleted', 'project', 'created']
    search_fields = ['project', 'describe']
    actions = ['mark_deleted']



@admin.register(News.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'deleted' ]
    ordering = ['title']
    list_per_page = 10
    list_filter = ['created', 'updated', 'deleted' ]
    search_fields = ['title', 'preamble', 'body']
    actions = ['mark_deleted']



@admin.register(News.NewsPicture)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['news', 'describe', 'picture', 'created']
    ordering = ['news']
    list_per_page = 10
    list_filter = ['news', 'describe', 'created']
    search_fields = ['news', 'describe']
    actions = ['mark_deleted']



    

@admin.register(Project.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = [ 'title', 'start_date', 'stop_date', 'map', 'house_area', 'material', 'bad', 'deleted']
    ordering = [ 'title', 'start_date']
    list_per_page = 10
    list_filter = [ 'created', 'deleted', 'material', 'bad' ]
    search_fields = ['title', 'body', 'start_date', 'stop_date', 'house_area']
    actions = ['mark_deleted']
    



# admin.site.register(User)