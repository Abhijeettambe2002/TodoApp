from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import EventForm
from events.models import Event
from django.contrib import messages


def user(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            login(request, user)
            return redirect("main_page")
    else:
        form = RegistrationForm()

    return render(request, "registration.html", {"form": form})


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("main_page")
    return render(request, "login.html")


def logout_page(request):
    logout(request)
    return redirect("login_page")


def main_page(request):
    if request.user.is_authenticated:
        events = Event.objects.filter(user=request.user)
        context = {
            "events": events,
            "has_events": events.exists(),
        }
        return render(request, "main_page.html", context)
    return render(request, "main_page.html")


def add_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect("main_page")
    else:
        form = EventForm()
    return render(request, "add_event.html", {"form": form})


def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    return redirect("main_page")


def update_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect("main_page")
    else:
        form = EventForm(instance=event)
    return render(request, "update_event.html", {"form": form})


def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, "event_details.html", {"event": event})
