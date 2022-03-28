from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html', {'name': 'Cory'})

def about(request):
    return render(request, 'about.html')

def proinfo(request):
    return render(request, 'proinfo.html')

def showcase(request):
    return render(request, 'showcase.html')

def survey(request):
    return render(request, 'survey.html')