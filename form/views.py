from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import User, Event, Round

# Create your views here.

def index(request):
    return render(request, 'form/index.html')

def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "form/login.html", {
                "message": "Invalid uInventePT/form/views.pysername and/or password."
            })
    
    return render(request, 'form/login.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

@login_required(login_url='login')
def eventform(request):
    if request.method == "POST":
        title = request.POST["title"]
        desc = request.POST["description"]
        ttype = request.POST["type"]
        dept = request.POST["dept"]
        rounds = int(request.POST["rounds"])
        team_size = request.POST["team_size"]
        dtype = request.POST["type_of_desc"]
        
        rounds_data = []

        for i in range(1, rounds+1):
            temp = {
                'title': request.POST["round{0}".format(i)],
                'desc': request.POST["round{0}-description".format(i)]
                }
            rounds_data.append(temp)

        venue = request.POST["venue"]
        date = request.POST["date"]
        first = request.POST["winner"]
        second = request.POST["runner"]
        third = request.POST["third"]

        try:
            eventt = Event.objects.create(title=title, description=desc, team_type=ttype, dept=dept, rounds=rounds, venue=venue, date=date, first_prize=first, second_prize=second, third_prize=third, team_size=team_size)
            eventt.save()
        except Exception:
            return render(request, 'form/event.html', {"error": Exception})
        for i in range(rounds):
            Round.objects.create(title=rounds_data[i]['title'], description=rounds_data[i]['desc'], event=eventt)

    return render(request, 'form/event.html')

@login_required(login_url='login')
def event(request, event_id):
    event = Event.objects.get(pk=event_id)
    rounds = Round.objects.filter(event=event)
    return render(request, 'form/eventpage.html', {"event": event, "rounds": rounds})

@login_required(login_url='login')
def events(request):
    if request.method == "POST":
        dept = request.POST["dept"]
        if dept == "all":
            events = Event.objects.all()
        else:
            events = Event.objects.filter(dept=dept)
        return render(request, 'form/events.html', {"events": events})
    return render(request, 'form/events.html')