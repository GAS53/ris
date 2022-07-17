from django.urls import path
from django.views.generic import RedirectView
from .views  import *
from django.conf import settings

app_name = 'mainapp'

# сделать RedirectView если страници не сущесвует или 404

urlpatterns = [
    path('', RedirectView.as_view(url='index/')),
    path('index/', IndexTemplateView.as_view(), name='index'),
    path('works/', WorksTemplateView.as_view(), name='works'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    
    # News CRUD
    path('news/list/', NewsListListView.as_view(), name='news_list'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news'),

    # Project CRUD
    path('project/list/', ProjectListView.as_view(), name='projects_list'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project'),


    # Feedback CRUD
    path('feedback/list/', FeedbackListListView.as_view(), name='feedback_list'),


]
