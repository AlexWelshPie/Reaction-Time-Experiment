from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    uniqueID        = models.AutoField(blank=True, primary_key=True)
    participantID   = models.ForeignKey(User, on_delete=models.CASCADE)
    representation  = models.CharField(max_length=100)
    numberofvalues  = models.CharField(max_length=100, default="Default value for numofval")
    repetition      = models.CharField(max_length=100, blank=True, null=True)
    values          = models.IntegerField(blank=True, null=True)
    correctanswer   = models.IntegerField(blank=True, null=True)
    answer          = models.IntegerField(blank=True, null=True)
    time            = models.IntegerField(blank=True, null=True)

    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.uniqueID

class Fruit(models.Model):
    name = models.CharField(max_length=255)
    amt = models.IntegerField()

    def __str__(self):
        return self.name