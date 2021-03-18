from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post
from .models import IndexView


def home(request):
    return render(request, 'patterns/home.html')


def about(request):
    if request.GET.get('Button') == 'Button':
        print('user clicked summary')
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'patterns/about.html', context)


def pygalexample(request):
    pygalobject = {
        'objects': IndexView.get_context_data(pygal2)
    }

    return render(request, 'patterns/pygalexample.html',pygalobject)
