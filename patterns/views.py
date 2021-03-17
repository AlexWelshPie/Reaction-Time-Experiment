from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'title': 'First Pattern is:',
        'content': 'This should be a square box',
    },
    {
        'title': 'Second Pattern is:',
        'content': 'This should be a square box',
    }
]
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'patterns/home.html', context)

def about(request):
    return render(request, 'patterns/about.html')