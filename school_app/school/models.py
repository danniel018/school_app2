from django.db import models 


class Children(models.Model):
    
    name = models.CharField(max_length=20,null=False)
    lastname = models.CharField(max_length=20,null=False)
    email = models.CharField(max_length=50,null=True)
    active = models.CharField(max_length=3,null=False)

    def __str__(self):
        return self.name + ' '  + self.lastname
    

class Users(models.Model):
    type_of_user = [('student','student'),('teacher','teacher'),('parent','parent')]
    name = models.CharField(max_length=20,null = False)
    lastname = models.CharField(max_length=20,null = False)
    email = models.CharField(max_length=50,null = False, unique = True)
    password = models.CharField(max_length=256,null = False)
    user_type = models.CharField(max_length=7,choices=type_of_user)

class GradeGroups(models.Model):
    
    name = models.CharField(max_length=3,null = False)
    director = models.ForeignKey(Users, on_delete=models.CASCADE) # Update foreign key
    year = models.IntegerField(null= False)
    classroom = models.CharField(max_length=5, null = True)
    children = models.ManyToManyField(Children)


class Subjects(models.Model):

    name = models.CharField(max_length=35,null = False)

class GradesSubjects(models.Model):

    grade_group = models.ForeignKey(GradeGroups, on_delete= models.CASCADE)
    subject = models.ForeignKey(Subjects, on_delete= models.CASCADE)
    teacher = models.ForeignKey(Users, on_delete= models.CASCADE)
    classroom = models.CharField(max_length=5, null = True)

class Events(models.Model):
    
    event_type = models.CharField(max_length=10)
    name = models.CharField(max_length=50,null=False)
    description = models.CharField(max_length=100,null=True)
    date = models.DateField(null=False)
    bimester = models.IntegerField(null=False)
    grade_subject = models.ForeignKey(GradesSubjects, on_delete = models.CASCADE) 
    

class Grades(models.Model):
    
    event = models.ForeignKey(Events, on_delete = models.CASCADE)
    child = models.ForeignKey(Children, on_delete = models.CASCADE)
    grade = models.FloatField(null= False)
    remarks = models.CharField(max_length=200, null=False)


class Announcements(models.Model):

    announcement_type = [('announcement','announcement'),('summons','summons')]
    type = models.CharField(max_length=12,choices=announcement_type)
    date = models.DateField(null = False)
    teacher = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    filelink = models.DateField(max_length=256, null = True)

class AnnouncementsChildren(models.Model):

    announcement = models.ForeignKey(Announcements, on_delete= models.CASCADE)
    child = models.ForeignKey(Children, on_delete= models.DO_NOTHING)
    grade_group = models.ForeignKey(GradeGroups, on_delete= models.CASCADE)
    