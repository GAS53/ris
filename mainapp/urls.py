from django.urls import path
from django.views.generic import RedirectView
import .views

app_name = 'mainapp'


urlpatterns = [
        path('', RedirectView.as_view(url='index')),
        path('index/', path(IndexTemplateView.as_view(), name='index'))
]