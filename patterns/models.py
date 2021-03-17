from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

        
$ python manage.py shell
>>> from charts_demo.models import Fruit
>>> Fruit(name='apples', amt=9).save()
>>> Fruit(name='oranges', amt=21).save()
>>> Fruit(name='pears', amt=15).save()
>>> Fruit(name='grapes', amt=12).save()
>>> Fruit(name='strawberries', amt=6).save()