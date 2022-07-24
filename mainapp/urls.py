from django.urls import path
from django.views.generic import RedirectView

from config.settings import CACHE_TIME as C_TIME
from .views  import *
from django.views.decorators.cache import cache_page


app_name = 'mainapp'



urlpatterns = [
    path('', RedirectView.as_view(url='index/')),

    path('index/', cache_page(C_TIME)(IndexTemplateView.as_view()), name='index'),
    path('works/', cache_page(C_TIME)(WorksTemplateView.as_view()), name='works'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    
    # News CRUD
    path('news/list/', cache_page(C_TIME)(NewsListListView.as_view()), name='news_list'),
    path('news/<int:pk>/', cache_page(C_TIME)(NewsDetailView.as_view()), name='news'),

    # Project CRUD
    path('project/list/', cache_page(C_TIME)(ProjectListView.as_view()), name='projects_list'),
    path('project/<int:pk>/', cache_page(C_TIME)(ProjectDetailView.as_view()), name='project'),


    # Feedback CRUD
    path('feedback/list/', cache_page(C_TIME)(FeedbackListListView.as_view()), name='feedback_list'),


]
