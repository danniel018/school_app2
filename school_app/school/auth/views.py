from django.core.cache import cache
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
  
from ..models import Users
from ..teachers.views import home as teachershome

def login_user(request):

    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request,email= email,           
                            password=password)
        if user is not None:
            login(request,user)
            messages.success(request, ("You Have Been Logged In!  Get MEEPING!"),'success') 
            return redirect(reverse ('teachers_home')) 

        else:
            messages.error(request,('error'),'danger')

        

    return render(request,'login.html')

@login_required(login_url='/auth/login/')
def logout_user(request):

    
    logout(request)
    cache.clear()

    
    return redirect(reverse ('login')) 
