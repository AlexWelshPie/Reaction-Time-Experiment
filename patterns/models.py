from django.db import models
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from pygal.style import DarkStyle
from .charts import FruitPieChart

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

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
        return context