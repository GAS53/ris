from django.views.generic import TemplateView, DeleteView, UpdateView, ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404
from random import choice
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
import urllib



from .models import News, Images, Project, Feedback
from random import choices

class IndexTemplateView(TemplateView):
    template_name = 'mainapp/index.html'

PICTURES_DICT = {}

def get_full_images_di():
    for image in Images.Image.objects.all():
        if PICTURES_DICT.get(image.work_type):
            PICTURES_DICT[image.get_work_type_display()].append(image)
        else:
            li = []
            li.append(image)
            PICTURES_DICT[image.get_work_type_display()] = li
    print(PICTURES_DICT)

def get_mini_di():
    mini_di = {}
    for typ, li_pictures in PICTURES_DICT.items():
        k = 3 if len(li_pictures) > 3 else len(li_pictures)
        mini_di[typ] = choices(li_pictures, k=k)
    return mini_di

class WorksTemplateView(TemplateView):
    template_name = 'mainapp/works.html'

    def get_context_data(self, **kwargs):
        context = super(WorksTemplateView, self).get_context_data()
        if PICTURES_DICT == {}:
            get_full_images_di()
        context['di_types'] = get_mini_di()
        return context




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


    def get_queryset(self, **kwargs):
        relation = self.request.GET.get('related', 'all')
        main_li = []
        for project in Project.Project.objects.all().filter(deleted=False):
            if project.house_type == relation or relation == 'all':
                fotos_object = Images.Image.objects.filter(project=project.pk)
                photos = []
                for foto in fotos_object.all():
                    photos.append(foto.image.url)
                one_photo = choice(photos) if len(photos) > 0 else '/media/images/one_for_all.jpg'
                main_li.append((project, photos, one_photo))
        return main_li




class ProjectDetailView(DetailView):
    template_name = 'mainapp/project.html'
    model = Project.Project

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data()
        li = []
        for image in Images.Image.objects.all():
            if image.project.pk == self.kwargs.get('pk'):
                li.append(image)
        context['li'] = li
        return context


   
class FeedbackListListView(ListView):
    template_name = 'mainapp/feedback_list.html'
    model = Feedback.FeedabckModel
    paginate_by = 5

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)
    
    
