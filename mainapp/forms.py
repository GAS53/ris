from django import forms
from .models import News, Images

class NewsForm(forms.ModelForm):

    class Meta:
        model = News.News
        fields = '__all__'


class ImagesForm(forms.ModelForm):

    class Meta:
        model = Images.Images
        fields = '__all__'



class ImagesForm(forms.ModelForm):

    class Meta:
        model = Images.Projects
        fields = '__all__'