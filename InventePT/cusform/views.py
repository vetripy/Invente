from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import User, Event, Round

# Create your views here.

def index(request):
    return render(request, 'cusform/index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "cusform/login.html", {
                "message": "Invalid uInventePT/cusform/views.pysername and/or password."
            })
    
    return render(request, 'cusform/login.html')

def logout(request):
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
            return render(request, 'cusoform/event.html', {"error": Exception})
        for i in range(rounds):
            Round.objects.create(title=rounds_data[i]['title'], description=rounds_data[i]['desc'], event=eventt)

    return render(request, 'cusform/event.html')