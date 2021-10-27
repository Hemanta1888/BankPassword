from django.db import models
from django import forms
from django.forms import widgets

class question_form(models.Model):
    questions = models.CharField(max_length=500)
    opt1 = models.CharField(max_length=200)
    opt2 = models.CharField(max_length=200)
    opt3 = models.CharField(max_length=200)
    opt4 = models.CharField(max_length=200)
    answer = (opt1,opt2,opt3,opt4)

    def __str__(self):
        return self.questions


    
    
