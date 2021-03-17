from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'patterns/home.html', context)

def about(request):
    return render(request, 'patterns/about.html')