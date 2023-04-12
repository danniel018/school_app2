from django.db import models 
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.hashers import make_password

class CustomUserManager(BaseUserManager): 
    def _create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)

        user = self.model( 
            email=self.normalize_email(email), 
        )

        user = self.model( email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,  email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False) 
        extra_fields.setdefault("is_superuser", False)
        return self._create_user( email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

class Users(AbstractUser):
    class Meta:
        db_table = 'users'

    type_of_user = [('student','student'),('teacher','teacher'),('parent','parent')]
    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=7,choices=type_of_user)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.first_name

    # def has_perm(self, perm, obj=None):
    #     return True

    # def has_module_perms(self, app_label):
    #     return True




class Children(models.Model):
    class Meta:
        db_table = 'children'
    
    name = models.CharField(max_length=20,null=False)
    lastname = models.CharField(max_length=20,null=False)
    email = models.CharField(max_length=50,null=True)
    active = models.CharField(max_length=3,null=False)

    def __str__(self):
        return self.name + ' '  + self.lastname
    

# class Users(models.Model):
#     type_of_user = [('student','student'),('teacher','teacher'),('parent','parent')]
#     name = models.CharField(max_length=20,null = False)
#     lastname = models.CharField(max_length=20,null = False)
#     email = models.CharField(max_length=50,null = False, unique = True)
#     password = models.CharField(max_length=256,null = False)
#     user_type = models.CharField(max_length=7,choices=type_of_user)

class GradeGroups(models.Model):

    class Meta:
        db_table = 'grade_groups'
    
    name = models.CharField(max_length=3,null = False)
    director = models.ForeignKey(Users, on_delete=models.CASCADE) # Update foreign key
    year = models.IntegerField(null= False)
    classroom = models.CharField(max_length=5, null = True)
    children = models.ManyToManyField(Children)


class Subjects(models.Model):
    class Meta:
        db_table = 'subjects'

    name = models.CharField(max_length=35,null = False)

class GradesSubjects(models.Model):
    class Meta:
        db_table = 'grades_subjects'

    grade_group = models.ForeignKey(GradeGroups, on_delete= models.CASCADE)
    subject = models.ForeignKey(Subjects, on_delete= models.CASCADE)
    teacher = models.ForeignKey(Users, on_delete= models.CASCADE)
    classroom = models.CharField(max_length=5, null = True)

class Events(models.Model):
    class Meta:
        db_table = 'class_events'

    event_type = models.CharField(max_length=10)
    name = models.CharField(max_length=50,null=False)
    description = models.CharField(max_length=100,null=True)
    date = models.DateField(null=False)
    bimester = models.IntegerField(null=False)
    grade_subject = models.ForeignKey(GradesSubjects, on_delete = models.CASCADE) 
    

class Grades(models.Model):
    class Meta:
        db_table = 'grades'

    event = models.ForeignKey(Events, on_delete = models.CASCADE)
    child = models.ForeignKey(Children, on_delete = models.CASCADE)
    grade = models.FloatField(null= False)
    remarks = models.CharField(max_length=200, null=False)


class Announcements(models.Model):
    class Meta:
        db_table = 'announcements'

    announcement_type = [('announcement','announcement'),('summons','summons')]
    type = models.CharField(max_length=12,choices=announcement_type)
    date = models.DateField(null = False)
    teacher = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    filelink = models.DateField(max_length=256, null = True)

class AnnouncementsChildren(models.Model):
    class Meta:
        db_table = 'announcements_children'

    announcement = models.ForeignKey(Announcements, on_delete= models.CASCADE)
    child = models.ForeignKey(Children, on_delete= models.DO_NOTHING)
    grade_group = models.ForeignKey(GradeGroups, on_delete= models.CASCADE)
    