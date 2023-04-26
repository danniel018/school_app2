from django.shortcuts import render
from django.http import HttpResponse 
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.db.models.functions import ExtractWeek

from datetime import datetime, date, timedelta, tzinfo, time
from zoneinfo import ZoneInfo
from ..models import Children, GradesSubjects, GradeGroups, ScheduleSubjects, \
    Users, Announcements, Events, Reports
# # Create your views here. 
@login_required(login_url='/auth/login/')
def home(request):

    teacher = Users.objects.filter(pk = request.user.id).first()# request.user
    print(teacher.first_name)

    today = date.today()
    week = today.isocalendar()[1]
    
    monday = datetime.fromisocalendar(today.year,week,1).strftime("%b %d %Y")
    friday = datetime.fromisocalendar(today.year,week,5).strftime("%b %d %Y") 

    schedule_classes = GradesSubjects.objects.filter(teacher = request.user.id).all()
    #schedule_classes = GradesSubjects.objects.filter(schedules__weekday = 'M').all()
    
    print(len(schedule_classes))
    #for x in schedule_classes[0]: 
    x = schedule_classes[0].schedulesubjects_set.all()  
    print(len(x)) 
    print(x[0].weekday)
    week_classes = []
    for subject in schedule_classes:
        for x in subject.schedulesubjects_set.all():
            print(x.weekday)
            daytime = datetime.fromisocalendar(today.year,week,x.weekday_iso) 
            #print(day[1])
            time_ = time.fromisoformat(x.start)
            #print(time_)
            daytime = daytime + timedelta(hours=time_.hour,minutes=time_.minute)
            week_classes.append(daytime)

    week_classes = sorted(week_classes) 

    next_classes = [x for x in week_classes if x > datetime.now()]

    if len(next_classes) == 0:
        upcoming_class = week_classes[0] + timedelta(weeks=1)
    else:
        upcoming_class = next_classes[0]

    upcoming_class = upcoming_class.strftime("%b %d %Y at %H:%M")
    announcements = Announcements.objects.annotate(week=ExtractWeek('date')).filter(
        week=week, date__year = today.year).all()
    
    events = Events.objects.annotate(week=ExtractWeek('date')).filter(
        week=week, date__year = today.year).all()
    
    laboratories = 0
    assessments = 0
    if len(events) > 0:
        laboratories = len( [x for x in events if x.event_type == 'laboratory'])
        assessments = len([x for x in events if x.event_type == 'exam'])

    reports = db.session.execute("SELECT COUNT(report_id) FROM reports WHERE "
        "WEEK(created_at,3) = WEEK(CURRENT_DATE,3)")
    reports = Reports.objects.annotate(week=ExtractWeek('created_at')).filter(
        week=week, date__year = today.year).all() 

    lessons = len(schedule_classes)
    events = len(events)
    issued_announcements = len(announcements)
    # z = [x.name for x in children]
    jack = [ 'all work and no play makes jack a dull boy' for _ in range(1,100)]
    context = {'data':jack,'next':upcoming_class}
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