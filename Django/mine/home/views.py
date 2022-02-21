from django.shortcuts import render, HttpResponse

def home (request):
    return render(request, 'index.html')

def about (request):
    return HttpResponse("This is the about page")

def contact (request):
    return HttpResponse("This is the contact page")

def product (request):
    return HttpResponse("This is the help page")

# Create your views here.
