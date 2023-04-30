from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from contentcontrol.models import assigned_record
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful")
            return HttpResponseRedirect("/")
        else:
            messages.success(request, "Error: Login Unsuccessful.")
            return HttpResponseRedirect("/")
    assigned_records = assigned_record.objects.all()
    return render(request, 'contentcontrol/index.html', {"assigned_records": assigned_records})

@csrf_exempt
def logout_user(request):
    logout(request)
    messages.success(request, 'Logout Successful.')
    return HttpResponseRedirect("/")

@csrf_exempt
def individual_record(request, id):
    if request.user.is_authenticated:
        record = assigned_record.objects.get(id = id)
        return render(request, 'contentcontrol/record.html', { 'record' : record })
    else:
        messages.success(request, "Error: Unauthorized Access.")
        return HttpResponseRedirect('/')

#add/delete for assigned entries
@csrf_exempt
def add_record(request):
    current_date = timezone.now()
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    email = request.POST["email"]
    address = request.POST["address"]
    city = request.POST["city"]
    state = request.POST["state"]
    zip = request.POST["zip"]
    assigned_to = request.POST["assigned_to"]
    notes = request.POST["notes"]
    
    if request.user.is_authenticated:
        created_object = assigned_record.objects.create(date_added = current_date, first_name = first_name, last_name = last_name, email = email, address = address, city = city, state = state, zip = zip, assigned_to = assigned_to, notes = notes)
        return HttpResponseRedirect("/")
    else:
        messages.success(request, "Error: Unauthorized Action.")
        return HttpResponseRedirect("/")

@csrf_exempt
def delete_record(request, id):
    if request.user.is_authenticated:
        assigned_record.objects.get(id = id).delete()
        return HttpResponseRedirect("/")
    else:
        messages.success(request, "Error: Unauthorized Action.")
        return HttpResponseRedirect("/")

@csrf_exempt
def update_record(request, id):
    if request.user.is_authenticated:
        record = assigned_record.objects.get(id = id)
        if request.method == 'POST':
            current_date = timezone.now()
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            email = request.POST["email"]
            address = request.POST["address"]
            city = request.POST["city"]
            state = request.POST["state"]
            zip = request.POST["zip"]
            assigned_to = request.POST["assigned_to"]
            notes = request.POST["notes"]
            assigned_record.objects.filter(id = id).update(date_added = current_date, first_name = first_name, last_name = last_name, email = email, address = address, city = city, state = state, zip = zip, assigned_to = assigned_to, notes = notes)
            return HttpResponseRedirect('/')
    else:
        messages.success(request, "Error: Unauthorized Access.")
        return HttpResponseRedirect('/')