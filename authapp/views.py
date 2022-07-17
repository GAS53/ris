from django.contrib.auth import get_user_model
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from authapp.forms import UserForm

class LoginView(LoginView):
    template_name = 'authapp/login.html'
    success_url = reverse_lazy('mainapp:index')
    

    def form_valid(self, form):
        # можно вставить сюда сообщения
        return HttpResponseRedirect(reverse_lazy("mainapp:crud"))

    def form_invalid(self, form):
        # можно вставить сюда сообщения
        return HttpResponseRedirect(reverse_lazy("mainapp:index"))


# class RegisterView(CreateView):
#     template_name = 'authapp/register.html'
#     model = get_user_model()
#     form_class = UserForm
#     success_url = reverse_lazy('mainapp:index')



# class EditView(LoginRequiredMixin, UpdateView):
#     template_name = 'authapp/edit.html'

# class LogoutView(LogoutView):
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)