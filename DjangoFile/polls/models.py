from random import choice
from tkinter.messagebox import QUESTION
from django.db import models

# Create your models here.
class Question (models.Model):
    question_text= models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    class choise (models.Model):
        question = models.ForeignKey( QUESTION , on_delete=models.CASCADE)
        choice_text = models.CharField(max_length=200)
        votes = models.IntegerField(default=0)


