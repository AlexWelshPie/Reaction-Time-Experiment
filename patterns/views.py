from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from pygal.style import DarkStyle
from .charts import FruitPieChart
from .models import Post


def home(request):
    return render(request, 'patterns/home.html')

def bubbleChart9(request):
    return render(request, 'patterns/bubbleChart9.html')

def bubble25(request):
    return render(request, 'patterns/bubble25.html')

def bubble5(request):
    return render(request, 'patterns/bubble5.html')


def about(request):
    if request.GET.get('Button') == 'Button':
        print('user clicked summary')
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'patterns/about.html', context)


def pygalexample(request):
    if request.method == 'POST':
        post = Post.objects.get()
        #post.uniqueID       = request.Post['uniqueID']
        #post.participantID  = request.Post['participantID']
        #post.representation = request.Post['representation']
        #post.numberofvalues = request.Post['numberofvalues']
        #post.repetition     = request.Post['repetition']
        #post.values         = request.Post['values']
        #post.correctanswer  = request.Post['correctanswer']
        #post.answer         = request.Post['answer']

        post.time           = request.Post['time']
        post.save()
        return HttpResponse('Updated!!')

    return render(request, 'patterns/pygalexample.html')
