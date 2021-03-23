from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from pygal.style import DarkStyle
from .charts import FruitPieChart
from .models import Post
from django.contrib.auth.models import User


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
        body = json.loads(request.body)
        post = Post.objects.create(
            time=body['time'],
            participantID=request.user,
            representation='c7',
            numberofvalues='h7',
            repetition='g7',
            values=12,
            correctanswer=15,
            answer=20
        )
        #post.uniqueID       = request.post['uniqueID']
        #post.participantID  = request.post['participantID']
        #post.representation = request.post['representation']
        #post.numberofvalues = request.post['numberofvalues']
        #post.repetition     = request.post['repetition']
        #post.values         = request.post['values']
        #post.correctanswer  = request.post['correctanswer']
        #post.answer         = request.post['answer']

       # post.time = body["time"]
        post.save()
        print(post.time)
        return HttpResponse('Updated!!')

    return render(request, 'patterns/pygalexample.html')
