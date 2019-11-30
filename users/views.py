from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import UserOurRegistration, ProfileUpdate, UserUpdateForm
from django.contrib import messages
from .models import Profile

def register(request):
    if request.method == "POST":
        form = UserOurRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('user')
    else:
            form = UserOurRegistration()
            form = UserOurRegistration()
    return render(request, 'users/registration.html', {'form': form, 'title': 'Регистрация пользователя'})


@login_required() #Декоратор, не дающий войти на страницу буз авторизации
def profile(request):
    if request.method == "POST":
        custom_profile = ProfileUpdate(request.POST, request.FILES, instance=request.user.profile) #Подставляем в поля существующие значения
        update_user = UserUpdateForm(request.POST, instance=request.user) #Подставляем в поля существующие значения

        if update_user.is_valid() and custom_profile.is_valid():
            custom_profile.save()
            update_user.save()
            messages.success(request, f'Ваш аккаунт был успешно обновлен')
            return redirect('profile')
    else:
        custom_profile = ProfileUpdate(instance=request.user.profile)
        update_user = UserUpdateForm(instance=request.user)
    data = {
        'custom_profile': custom_profile,
        'update_user': update_user
    }

    return render(request, 'users/profile.html', data)


def list(request):
    data = {
        'guys': Profile.objects.all()
    }
    return render(request, 'users/list.html', data)


