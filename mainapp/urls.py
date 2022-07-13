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
    path('news/create/', NewsCreateView.as_view(), name='news_create'),
    path('news/list/', NewsListListView.as_view(), name='news_list'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news'),
    path('news/<int:pk>/update/', NewsUpdateView.as_view(), name='news_update'),
    path('news/<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),

    # Project CRUD
    path('project/create/', ProjectCreateView.as_view(), name='project_create'),
    path('project/list/', ProjectListListView.as_view(), name='projects_list'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),

    # Images CRUD
    path('image/create/', ImagesCreateView.as_view(), name='image_create'),
    path('image/<int:pk>/delete/', ImagesDeleteView.as_view(), name='image_delete'),

    # Feedback CRUD
    path('feedback/create/', FeedbackCreateView.as_view(), name='feedback_create'),
    path('feedback/list/', FeedbackListListView.as_view(), name='feedback_list'),
    path('feedback/<int:pk>/update/', FeedbackUpdateView.as_view(), name='feedback_update'),
    path('feedback/<int:pk>/delete/', FeedbackDeleteView.as_view(), name='feedback_delete'),



    # dop
    path('image/create/', AdminNews.as_view(), name='news_edit'),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
