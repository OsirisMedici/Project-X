from django.shortcuts import render
from django.http import HttpResponse


def index (request):
    return HttpResponse('hello World, We are here.. and you are at the Polls Index')
