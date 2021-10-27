from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from .models import forms

def home_page(request):
    return render(request,'homepage.html')

def view_form(request):
    if request.method == 'POST':
        form = question_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('quiz:Submit'))
    model_data = question_form.objects.all()
    return render(request,'questions.html',{
        'model':model_data
    })



def submit_data(request):
    return render(request,'submit.html')