from django.shortcuts import render
from .models import Post

def main(request):
    data = {
        'news': Post.objects.all()
    }
    return render(request, 'home/main.html', data)

def price(request):
    return render(request, 'home/price.html')

def about(request):
    return render(request, 'home/about.html')
