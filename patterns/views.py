from django.shortcuts import render
from pygal.style import DarkStyle
from .charts import FruitPieChart
from .models import Post


def home(request):
    return render(request, 'patterns/home.html')

def bubbleChart9(request):
    return render(request, 'patterns/bubbleChart9.html')


def about(request):
    if request.GET.get('Button') == 'Button':
        print('user clicked summary')
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'patterns/about.html', context)


def pygalexample(request):
    context = {}

    # Instantiate our chart. We'll keep the size/style/etc.
    # config here in the view instead of `charts.py`.
    cht_fruits = FruitPieChart(
        height=600,
        width=800,
        explicit_size=True,
        style=DarkStyle
    )

    # Call the `.generate()` method on our chart object
    # and pass it to template context.
    context['cht_fruits'] = cht_fruits.generate()
    return render(request, 'patterns/pygalexample.html', context)
