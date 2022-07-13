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

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()