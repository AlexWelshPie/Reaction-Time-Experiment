from django.shortcuts import render
from .models import Post


def home(request):
    return render(request, 'patterns/home.html')

def about(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'patterns/about.html', context)