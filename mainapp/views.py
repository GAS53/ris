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


class NewsCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'mainapp/news_create.html'
    model = News.News
    fields = "__all__"
    success_url = reverse_lazy("mainapp:news_list")


class NewsListListView(ListView):
    template_name = 'mainapp/news_list.html'
    model = Images.Image
    paginate_by = 6

    def get_queryset(self):
        all = Images.Image.objects.all#
        return super().get_queryset().filter(deleted=False)


class NewsDetailView(DetailView):
    template_name = 'mainapp/news.html'
    model = News.News


class NewsUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'mainapp/news_update.html'
    model = News.News
    fields = "__all__"
    success_url = reverse_lazy("mainapp:news_list")


class NewsDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'mainapp/news_delete.html'
    model = News.News
    success_url = reverse_lazy("mainapp:news_list")
    permission_required = ("mainapp.news_delete",)


class ProjectCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'mainapp/project_create.html'
    model = Project.Project
    fields = "__all__"
    success_url = reverse_lazy("mainapp:projects_list")
    permission_required = ("mainapp.project_create",)


class ProjectListListView(ListView):
    template_name = 'mainapp/projects_list.html'
    model = Project.Project
    paginate_by = 6

    def get_queryset(self):
        main_li = []
        for project in Project.Project.objects.all().filter(deleted=False):
            fotos_object = Images.Image.objects.filter(project=project.pk)
            photos = []
            for foto in fotos_object.all():
                photos.append(foto.path.url)
            one_photo = choice(photos) if len(photos)>0 else '/media/images/one_for_all.jpg'
            main_li.append((project, photos, one_photo))
        return main_li


class ProjectDetailView(DetailView):
    template_name = 'mainapp/project.html'
    model = Project.Project


class ProjectUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'mainapp/project_update.html'
    model = Project.Project
    fields = "__all__"
    permission_required = ("mainapp.project_update",)

    def get_success_url(self):
        return reverse_lazy("mainapp:project_update", args=[self.request.user.pk])



class ProjectDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'mainapp/project_delete.html'
    model = Project.Project
    success_url = reverse_lazy("mainapp:project_delete")
    permission_required = ("mainapp.project_delete",)



class ImagesCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'mainapp/image_create.html'
    model = Images.Image
    fields = "__all__"
    success_url = reverse_lazy("mainapp:image_create")
    permission_required = ("mainapp.image_create",)


class ImagesDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'mainapp/image_delete.html'
    model = Images.Image
    success_url = reverse_lazy("mainapp:image_delete")
    permission_required = ("mainapp.image_delete",)


class FeedbackCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'mainapp/feedback_create.html'
    model = Feedback.FeedabckModel
    fields = "__all__"
    success_url = reverse_lazy("mainapp:feedback_create")
    permission_required = ("mainapp.feedback_create",)

   
class FeedbackListListView(ListView):
    template_name = 'mainapp/feedback_list.html'
    model = Feedback.FeedabckModel
    paginate_by = 5

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)
    
    
class FeedbackUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'mainapp/feedback_update.html'
    model = Feedback.FeedabckModel
    fields = "__all__"
    permission_required = ("mainapp.feedback_update",)

    def get_success_url(self):
        return reverse_lazy("mainapp:feedback_update", args=[self.request.user.pk])


class FeedbackDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'mainapp/feedback_delete.html'
    model = Feedback.FeedabckModel
    success_url = reverse_lazy("mainapp:feedback_delete")
    permission_required = ("mainapp.feedback_delete",)






class AdminNews(TemplateView):
    template_name = 'admin/mainapp/news/'

