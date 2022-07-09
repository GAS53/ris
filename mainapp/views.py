from django.views.generic import TemplateView, ListView, DetailView
from .models import News
from django.shortcuts import get_object_or_404


class IndexTemplateView(TemplateView):
    template_name = 'mainapp/index.html'

class WeTemplateView(TemplateView):
    template_name = 'mainapp/we.html'

class GaleryTemplateView(TemplateView):
    template_name = 'mainapp/galery.html'

class ContactsTemplateView(TemplateView):
    template_name = 'mainapp/contacts.html'

class WorksTemplateView(TemplateView):
    template_name = 'mainapp/works.html'




class NewsListTemplateView(ListView):
    template_name = 'mainapp/news_list.html'
    model = News
    paginate_by = 6

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)

class NewsTemplateView(DetailView):
    model = News
    template_name = 'mainapp/news.html'