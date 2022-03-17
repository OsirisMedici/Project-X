from django.shortcuts import render, HttpResponse

def index (request):
    return HttpResponse("This page is for Team Members")