from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def new(request):
    return render(request,'new_survey.html')