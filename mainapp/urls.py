from django.urls import path
from django.views.generic import RedirectView
from .views import IndexTemplateView, WorksTemplateView, NewsTemplateView, WeTemplateView, GaleryTemplateView, ContactsTemplateView


app_name = 'mainapp'


urlpatterns = [
        path('', IndexTemplateView.as_view(), name='index'),
        path('works/', WorksTemplateView.as_view(), name='works'),
        path('we/', WeTemplateView.as_view(), name='we'),
        path('galery/', GaleryTemplateView.as_view(), name='galery'),
        path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
        path('news/', ContactsTemplateView.as_view(), name='news'),
]