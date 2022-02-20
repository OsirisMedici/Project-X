from django.shortcuts import render, HttpResponse

def index (request):
    return HttpResponse("This is the Home page")

# Create your views here.
