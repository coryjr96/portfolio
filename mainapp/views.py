import email
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm, SnippetForm
from django.views.decorators.csrf import csrf_exempt

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

@csrf_exempt
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            print(name, email)

    form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def snippet_detail(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            print("VALID")

    form = SnippetForm()
    return render(request, 'contact.html', {'form': form})