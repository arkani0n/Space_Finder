from django.shortcuts import render
from django.views.generic import RedirectView,DetailView,ListView,CreateView
from main.models import *
# Create your views here.
from main.models import *





def all_planets(request):
    planets=Planet.objects.all()
    return  render(request,'info/planet_list.html',{'planets':planets})


def all_stars(request):
    stars=Star.objects.all()
    return  render(request,'info/star_list.html',{'stars':stars})

def planet(request,pk):
    planet = Planet.objects.get(id=pk)
    star_system= planet.star_set.all()
    contex={
        'planet': planet,
        'star_system': star_system,
        'last_star': list(star_system)[-1]
    }
    return render(request,'info/planet_detail.html', contex)

def star(request,pk):
    star = Star.objects.get(id=pk)
    star_system= star.star_system.all()
    contex={
        'star': star,
        'star_system': star_system,
        'last_planet': list(star_system)[-1]
    }
    return render(request,'info/star_detail.html', contex)


class PlanetListView(ListView):
    model = Planet
    template_name = 'info/planet_list.html'
    context_object_name = 'planets'

class PlanetDetailView(DetailView):
    model = Planet
    template_name = 'info/planet_detail.html'

    def get_context_data(self, **kwargs):
        contex=super().get_context_data(**kwargs)
        star_system = self.object.star_set.all()
        contex['star_system']=star_system
        contex['last_star']= list(star_system)[-1]
        return contex


class StarListView(ListView):
    model = Star
    context_object_name = 'stars'
    template_name = 'info/star_list.html'


class StarDetailView(DetailView):
    model = Star
    template_name = 'info/star_detail.html'

    def get_context_data(self, **kwargs):
        contex=super().get_context_data(**kwargs)
        star_system = self.object.star_system.all()
        contex['star_system']=star_system
        contex['last_planet']=list(star_system)[-1]
        return contex

class Create(CreateView):
    model = Planet
    template_name = 'info/planet_form'
    queryset = Planet.objects.all()