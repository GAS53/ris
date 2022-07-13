from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('admin/', include('authapp.urls', namespace='authapp')),
    path('', RedirectView.as_view(url='mainapp/')),
    path('mainapp/', include('mainapp.urls', namespace='mainapp')),
]

