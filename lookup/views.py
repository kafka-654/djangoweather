from django.shortcuts import render
#This is a views file.

def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})