from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserOurRegistration(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']




class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdate(forms.ModelForm):

    #Меняем название поля
    def __init__(self, *args, **kwargs):
        super(ProfileUpdate, self).__init__(*args, **kwargs)
        self.fields['img'].label = "Изображение профиля"


    class Meta:
        model = Profile
        fields = ['img', 'name', 'portfoils_site', 'ready', 'job', 'exp', 'price', 'about']