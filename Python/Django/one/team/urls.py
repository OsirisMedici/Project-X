from django.contrib import admin
from django.urls import path 
from team import views
import team

urlpatterns = [
     path('', views.index, name=team)
]
