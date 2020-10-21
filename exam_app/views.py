from django.shortcuts import render, redirect
from .models import User, Trip
from django.contrib import messages

def mainpage(request):

    return render(request, "index.html")

def gohere(request):

    return redirect("/main")

def create(request):
    errors = User.objects.RegisterValidator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/main")

    else:
        newUser = User.objects.create(name = request.POST['name'], username = request.POST['usernameReg'], password = request.POST['passwordReg'])
        request.session['User_username'] = request.POST['usernameReg']

    return redirect("/travels")

def login(request):
    errors = User.objects.loginValidator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/main")

    request.session['User_username'] = request.POST['usernameLog']

    return redirect("/travels")

def userpage(request):
    loggedinUser = User.objects.get(username = request.session['User_username'])

    context = {
        "user" : loggedinUser,
        "user_trips" : Trip.objects.filter(user = loggedinUser),
        "other_trips" : Trip.objects.exclude(user = loggedinUser)
    }


    return render(request, "userpage.html", context)

def logout(request):

    return redirect("/main")

def addtrip(request):

    return render(request, "addtrip.html")

def addtriptouser(request, trip_id):
    loggedinUser = User.objects.get(username = request.session['User_username'])

    d = Trip.objects.get(id=trip_id)

    loggedinUser.trips.add(d)

    return redirect("/travels")

def homepage(request):

    return redirect("/travels")

def addingAtrip(request):
    loggedinUser = User.objects.get(username = request.session['User_username'])
    errors = Trip.objects.tripValidator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/travels/add")

    else:
        newTrip = Trip.objects.create(planned_by = loggedinUser.name, destination = request.POST['destination'], desc = request.POST['description'], travel_date_from = request.POST['datefrom'], travel_date_to = request.POST['dateto'])

    return redirect("/travels")

def trippage(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    context = {
        "trip" : Trip.objects.get(id=trip_id),
        "trip_users" : User.objects.filter(trips = trip)
    }

    return render(request, "trippage.html", context)