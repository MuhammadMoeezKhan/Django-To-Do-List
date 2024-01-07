from django.shortcuts import render, HttpResponse
from .models import TodoItem

def home(request):
    return render(request, "home.html")

def todoitems(request):
    items = TodoItem.objects.all()
    return render(request, "todoitems.html", {"todos" : items})