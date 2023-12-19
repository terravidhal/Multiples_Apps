from django.shortcuts import render, HttpResponse, redirect # add redirect to import statement
from django.http import JsonResponse

# Create your views here.

def index(request):
    return HttpResponse("Placeholer to later deploy a list of blogs")

def new(request):
    return HttpResponse("Placeholer to later deploy a new blog form")

def create(request):
    return redirect('/')

def show(request, number):
    return HttpResponse(f"Placeholer to display blog num {number}")

def edit(request, number):
    return HttpResponse(f"Placeholer to edit blog num {number}")

def destroy(request, number):
    return redirect('/blogs')

def bonus(request):
    return JsonResponse({'title': 'my first blog', 'content': 'bla bla bla'})