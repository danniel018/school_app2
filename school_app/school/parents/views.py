from django.shortcuts import render
from django.http import HttpResponse 

def home(request):

    # children = Children.objects.all()

    # z = [x.name for x in children]

    return HttpResponse ('<h1 style="color:red;">fuck you a hundred times</h1>')

