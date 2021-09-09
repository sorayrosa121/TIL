# articles/forms.py

from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta: # form에 대한 정보
        model = Article
        fields = '__all__'

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'placeholder':'Enter the Title'}))
#     content = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Enter the Content'}))
#     image = forms.ImageField()