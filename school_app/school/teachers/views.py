from django.shortcuts import render
from django.http import HttpResponse 
from django.utils import timezone
from datetime import datetime, date, timedelta, tzinfo
from zoneinfo import ZoneInfo
from ..models import Children, GradesSubjects, GradeGroups
# # Create your views here. 

def home(request):


    # z = [x.name for x in children]
    jack = [ 'all work and no play makes jack a dull boy' for _ in range(1,100)]
    context = {'data':jack}
    return render (request,'teachers/home.html',context)


def classes(request):

    Zone = ZoneInfo('America/Bogota')
    now = timezone.now().astimezone(Zone) 
    year = (now.date().year)
    #x = datetime.now().astimezone(ZoneInfo('Asia/Tokyo'))
    
    #classes = GradesSubjects.objects.filter(teacher = )
    # print(classes)
    return HttpResponse ('Tankard')