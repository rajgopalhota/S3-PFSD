from imp import source_from_cache
from tokenize import Name
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
import datetime
from .models import  ScheduleRide,OnTheGo

# Create your views here.
def LoginView(request):
    if request.method == 'POST':
        username = request.POST['mail']
        password = request.POST['passwd']
        user = auth.authenticate(username = username, password =password)
        print(username, password)
        if user is not None:
            auth.login(request , user)
            return redirect('/home')
        else:
            messages.info(request, 'invalid username or password')
            return redirect("/")
    else:
        return render(request,'Rentals/login.html')

def Register(request):
    if request.method == 'POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email = request.POST['mail']
        username = request.POST['username']
        password1= request.POST['password1']
        password2= request.POST['password2']
        if password1==password2:
            password = password1
        else:
            messages.info(request, 'Passwords dont match')
        date = datetime.date.today()

        user = User.objects.create_user(first_name = fname, last_name = lname, username = username , password = password , email = email, date_joined = date)
        user.save()
        print('user created')
        return redirect('/')

    return render(request,'Rentals/register.html')

def Home(request):
    return render(request, 'Rentals/home.html')

def Ridenow(request):
    if request.method == 'POST':
        srce = request.POST['o_from']
        dest = request.POST['o_dest']
        type = request.POST['o_optedcar']
        phone = request.POST['o_phone']
        booking = datetime.datetime.today()
        print(srce, dest, type, phone, booking)
        ride = OnTheGo(source = srce, destination = dest, cartype = type, phone = phone)
        ride.save()

    return render(request, 'Rentals/OnTheGo.html')

def Ridelater(request):
    if request.method == 'POST':
        srce = request.POST['s_from']
        dest = request.POST['s_dest']
        sdate = str(request.POST['s_date'])
        stime = str(request.POST['s_time'])
        type = request.POST['s_optedcar']
        phone = request.POST['s_phone']
        booking = datetime.datetime.today()
        print(srce, dest, sdate, stime, type, phone, booking)
        ride = ScheduleRide(source = srce, destination = dest,date = sdate,time = stime, cartype = type, phone = phone)
        ride.save()
        messages.success(request, 'Bokked a cab')
    return render(request, 'Rentals/schedule.html')

