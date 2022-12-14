from django import forms
from .models import News, Images, Base

class NewsForm(forms.ModelForm):

    class Meta:
        model = News.News
        fields = '__all__'


class ImagesForm(forms.ModelForm):

    class Meta:
        model = Images.Image
        fields = '__all__'



class ImagesForm(forms.ModelForm):

    class Meta:
        model = Images.Project
        fields = '__all__'



class Email_me_Form(forms.Form):
    email = forms.EmailField(label="Ваша почта для обратной связи")
    name = forms.CharField(max_length=70, label="ФИО")
    question = forms.CharField(label='Задайте нам вопрос', max_length=1000)
    work_type = forms.ModelChoiceField(queryset=Base.Base_work.objects.all(), label='Типы работ')
    material_type = forms.ModelChoiceField(queryset=Base.Base_matherials.objects.all(), label='Основной материал')



    
