from django.shortcuts import render,HttpResponse, redirect


# Create your views here.

def root(request):
    return redirect('/blogs')

def register(request):
    return HttpResponse("Placeholer to register")

def login(request):
    return HttpResponse("Placeholer to log in")

def show(request):
    return HttpResponse("Show all users")