from django.shortcuts import render, HttpResponse

def home (request):
    return HttpResponse("This is the Home page")

def about (request):
    return HttpResponse("This is the about page")

def contact (request):
    return HttpResponse("This is the contact page")

def help (request):
    return HttpResponse("This is the help page")

# Create your views here.
