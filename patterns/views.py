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
    if request.method == 'POST':
        body = json.loads(request.body)
        post = Post.objects.create(
            time=body['time'],
            participantID=request.user,
            representation='Bubble',
            numberofvalues='n9',
            repetition=body['repetition'],
            values=body['values'],
            correctanswer=body['correctanswer'],
            answer=body['answer']
        )
        post.save()
        print(post.time)
        return HttpResponse('Saved answers for Bubble 9')
    return render(request, 'patterns/bubbleChart9.html')

def bubble25(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        post = Post.objects.create(
            time=body['time'],
            participantID=request.user,
            representation='Bubble',
            numberofvalues='n25',
            repetition=body['repetition'],
            values=body['values'],
            correctanswer=body['correctanswer'],
            answer=body['answer']
        )
        post.save()
        print(post.time)
        return HttpResponse('Saved answers for Bubble 25')
    return render(request, 'patterns/bubble25.html')

def bubble5(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        post = Post.objects.create(
            time=body['time'],
            participantID=request.user,
            representation='Bubble',
            numberofvalues='n5',
            repetition=body['repetition'],
            values=body['values'],
            correctanswer=body['correctanswer'],
            answer=body['answer']
        )
        post.save()
        print(post.time)
        return HttpResponse('Saved answers for Bubble 5')
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
            representation='Bubble',
            numberofvalues='n3',
            repetition=body['repetition'],
            values=body['values'],
            correctanswer=body['correctanswer'],
            answer=body['answer']
        )
        post.save()
        print(post.values)
        return HttpResponse('Updated answer for Bubble 3')

    return render(request, 'patterns/pygalexample.html')

def text3(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        post = Post.objects.create(
            time=body['time'],
            participantID=request.user,
            representation='Bubble',
            numberofvalues='n3',
            repetition=body['repetition'],
            values=body['values'],
            correctanswer=body['correctanswer'],
            answer=body['answer']
        )
        post.save()
        print(post.values)
        return HttpResponse('Updated answer for Text 3')

    return render(request, 'patterns/text3.html')

def text5(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        post = Post.objects.create(
            time=body['time'],
            participantID=request.user,
            representation='Bubble',
            numberofvalues='n3',
            repetition=body['repetition'],
            values=body['values'],
            correctanswer=body['correctanswer'],
            answer=body['answer']
        )
        post.save()
        print(post.values)
        return HttpResponse('Updated answer for Text 5')

    return render(request, 'patterns/text5.html')

def text9(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        post = Post.objects.create(
            time=body['time'],
            participantID=request.user,
            representation='Bubble',
            numberofvalues='n3',
            repetition=body['repetition'],
            values=body['values'],
            correctanswer=body['correctanswer'],
            answer=body['answer']
        )
        post.save()
        print(post.values)
        return HttpResponse('Updated answer for Text 9')

    return render(request, 'patterns/text9.html')

def text25(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        post = Post.objects.create(
            time=body['time'],
            participantID=request.user,
            representation='Bubble',
            numberofvalues='n3',
            repetition=body['repetition'],
            values=body['values'],
            correctanswer=body['correctanswer'],
            answer=body['answer']
        )
        post.save()
        print(post.values)
        return HttpResponse('Updated answer for Text 25')

    return render(request, 'patterns/text25.html')