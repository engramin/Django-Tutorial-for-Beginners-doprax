from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.decorators import login_required


# from musiclibrary.song.models import Artist


def hello_world(request):
    return HttpResponse("Hello World!")


def home(request):
    return render(request, "index.html")


def artist(request):
    # artist_list = Artist.objects.all()

    context = {'artist_list': artist_list}

    return render(request, 'index.html', context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('home')
    else:
        form = AuthenticationForm()
        return render(request, 'signin.html', {'form': form})
