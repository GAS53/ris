from django.urls import path
from authapp.views import LoginView# , RegisterView, LogoutView, EditView
from django.contrib import admin
    


app_name = 'authapp'

urlpatterns = [
    # path('admin/', admin.site.urls, name='admin'),
    path('', LoginView.as_view(), name='login'),
    
    # path('register/', RegisterView.as_view(), name='register'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    # path('edit/', EditView.as_view(), name='edit'),

]

