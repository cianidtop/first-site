from django import forms
from .models import Wedding, Film







class WeddingClass(forms.ModelForm):

    class Meta:
        model = Wedding
        fields = ['title', 'text', 'video']


class FilmClass(forms.ModelForm):

    class Meta:
        model = Wedding
        fields = ['title', 'text', 'video']