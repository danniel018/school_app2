from django.shortcuts import render
from django.http import HttpResponse 
# from .models import Children
# # Create your views here. 

def home(request):

    # children = Children.objects.all()

    # z = [x.name for x in children]

    return render (request,'teachers/home.html')


def classes(request):

    y={'x':['ARG','COL']}

    return HttpResponse ('Tankard')