from django.contrib import admin
from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'rubric', 'preamble', 'body', 'picture', 'created', 'updated', 'deleted' ]
    ordering = ['title', 'preamble']
    list_per_page = 10
    list_filter = ['rubric', 'created', 'updated', 'deleted' ]
    search_fields = ['title', 'preamble', 'body']
    actions = ['mark_deleted']