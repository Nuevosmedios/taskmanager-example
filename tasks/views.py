from django.shortcuts import render
from django.views.generic import CreateView
from .models import Task

class TaskCreate(CreateView):
    model = Task
    success_url = '/'
