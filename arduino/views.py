from django.shortcuts import render, redirect
from .models import *
import pyfirmata
from time import sleep


def timer(t) : 
    while t!=0:
        t=t-1
        sleep(1)
    False

color = 'white'


def compt(request, slug):
    global color
    equipe = Match.objects.get(code=slug)
    return render(request, 'arduino/compt.html', {'equipe':equipe, 'color':color})

def red(request, slug):
    global color
    print(color)
    color = 'red'
    return redirect('jury', slug)
    

def blue(request, slug):
    global color
    print(color)
    color = 'blue'
    return redirect('jury', slug)


def start(request):
    if request.method == "POST":
        code = request.POST.get("code")

        return redirect("compt", code)
    
    return render(request, 'arduino/start.html')    

def points(request, slug, pt):
    equipe = Match.objects.get(code=slug)
    pt = [-5, 5, 10, 25, 50]
    if request.method == "POST":
        name = request.POST.get("equipe")
        if name == equipe.teamBlue:
            p = equipe.scoreB+pt
            equipe.scoreB=p
            equipe.save()
        else:
            p = equipe.scoreR+pt
            equipe.scoreR = p
            equipe.save()

        return redirect("jury", slug,)

    return render(request, 'arduino/jury.html', {'equipe':equipe, 'pt':pt})

def jury(request, slug):
    equipe = Match.objects.get(code=slug)

    return render(request, 'arduino/jury.html', {'equipe':equipe})

def func(c):
    global color
    color = c
