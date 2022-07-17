from django.views.generic import TemplateView, DeleteView, UpdateView, ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404
from random import choice
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import News, Images, Project, Feedback


class IndexTemplateView(TemplateView):
    template_name = 'mainapp/index.html'

class WorksTemplateView(ListView): 
    template_name = 'mainapp/works.html'
    model = Images.Image


    def get_queryset(self):

        return super().get_queryset().filter(deleted=False)


class ContactsTemplateView(TemplateView):
    template_name = 'mainapp/contacts.html'



class NewsListListView(ListView):
    template_name = 'mainapp/news_list.html'
    model = News.News
    paginate_by = 6

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class NewsDetailView(DetailView):
    template_name = 'mainapp/news.html'
    model = News.News





class ProjectListView(ListView):
    template_name = 'mainapp/projects_list.html'
    model = Project.Project
    paginate_by = 6

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(num=num, **kwargs)
    #     self.num = context['num']
    #     return context
# здесь нужно разобраться как получить из html num который будет по умолчанию
# 'all' или 'br' bl fr для различных типов домов и возвращать исходя из этого
# get_queryset

    def get_queryset(self, **kwargs):
        relation = self.request.GET.get('relation', None)
        print(relation)
        main_li = []
        for project in Project.Project.objects.all().filter(deleted=False):
            if project.house_type == relation or relation == 'all':
                fotos_object = Images.Image.objects.filter(project=project.pk)
                photos = []
                for foto in fotos_object.all():
                    photos.append(foto.image.url)
                one_photo = choice(photos) if len(photos)>0 else '/media/images/one_for_all.jpg'
                main_li.append((project, photos, one_photo))
        return main_li




class ProjectDetailView(DetailView):
    template_name = 'mainapp/project.html'
    model = Project.Project



   
class FeedbackListListView(ListView):
    template_name = 'mainapp/feedback_list.html'
    model = Feedback.FeedabckModel
    paginate_by = 5

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)
    
    
