
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('authapp/', include('authapp.urls', namespace='authapp')),
    path('', RedirectView.as_view(url='mainapp/')),
    path('mainapp/', include('mainapp.urls', namespace='mainapp')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    import debug_toolbar

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
    urlpatterns.append(path("__debug__/", include(debug_toolbar.urls)))
else:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()