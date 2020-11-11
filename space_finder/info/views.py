from django.shortcuts import render
from django.views.generic import RedirectView,DetailView
from main.models import *
# Create your views here.
from main.models import *





def all_planets(request):
    planets=Planet.objects.all()
    return  render(request,'info/all_planets.html',{'planets':planets})


def all_stars(request):
    stars=Star.objects.all()
    return  render(request,'info/all_stars.html',{'stars':stars})

def planet(request,pk):
    planet = Planet.objects.filter(id=pk)[0]
    star_system= planet.star_set.all()
    contex={
        'planet': planet,
        'star_system': star_system
    }
    return render(request,'info/planet.html', contex)

def star(request,pk):
    star = Star.objects.filter(id=pk)[0]
    star_system= star.star_system.all
    contex={
        'star': star,
        'star_system': star_system
    }
    return render(request,'info/star.html', contex)