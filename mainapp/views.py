from django.views.generic import TemplateView


class IndexTemplateView(TemplateView):
    template_name = 'mainapp/index.html'

class WeTemplateView(TemplateView):
    template_name = 'mainapp/we.html'

class GaleryTemplateView(TemplateView):
    template_name = 'mainapp/galery.html'

class ContactsTemplateView(TemplateView):
    template_name = 'mainapp/contacts.html'

class WorksTemplateView(TemplateView):
    template_name = 'mainapp/works.html'

class NewsTemplateView(TemplateView):
    template_name = 'mainapp/news.html'