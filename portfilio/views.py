from django.shortcuts import render
from .models import Wedding, Film

def portfolio(request):
    return render(request, 'portfilio/portfolio.html')


def weddings(request):
    data = {
        'news': Wedding.objects.all()
    }
    return render(request, 'portfilio/weddings.html', data)



def films(request):
    data = {
        'news': Film.objects.all()
    }
    return render(request, 'portfilio/films.html', data)


