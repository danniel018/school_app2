from django.shortcuts import render
from django.http import HttpResponse 
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from datetime import datetime, date, timedelta, tzinfo
from zoneinfo import ZoneInfo
from ..models import Children, GradesSubjects, GradeGroups, ScheduleSubjects 
# # Create your views here. 
@login_required(login_url='/auth/login/')
def home(request):

    schedules = ScheduleSubjects.objects.filter(weekday = 'TU').all()
    for x in schedules:

        print(x.weekday, x.start, x.end)
    # z = [x.name for x in children]
    jack = [ 'all work and no play makes jack a dull boy' for _ in range(1,100)]
    context = {'data':jack,'schedules':schedules}
    return render (request,'teachers/home.html',context)

@login_required(login_url='/auth/login/')
def classes(request):

    Zone = ZoneInfo('America/Bogota')
    now = timezone.now().astimezone(Zone) 
    year = (now.date().year)
    #x = datetime.now().astimezone(ZoneInfo('Asia/Tokyo'))
    
    #classes = GradesSubjects.objects.filter(teacher = )
    # print(classes)
    return render (request,'teachers/classes.html')