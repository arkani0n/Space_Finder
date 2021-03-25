from django.shortcuts import render,redirect
from main.models import *
from django.http import HttpRequest


def search_page(request):
    if request.method=='GET':
        return render(request,'search/search_page.html', {'found': None})
    else:
        fiend = find(request)
        return fiend


def find(request : HttpRequest):
    req_post=request.POST
    d={
        'star': Star.objects.all(),
        'planet': Planet.objects.all()
    }
    planet_or_star = req_post.get('space_obj',None)

    if planet_or_star != 'star' and  planet_or_star !='planet':
        return redirect('search')

    elif planet_or_star=='star':
        is_star = 1
        is_planet = 0
    elif planet_or_star=='planet':
        is_star = 0
        is_planet = 1

    all_obj=d[planet_or_star]

    name=req_post['search_for']
    print(name,planet_or_star)
    found=all_obj.filter(name__icontains=name)
    return render(request, 'search/search_page.html', {
                'found': found,
                'is_planet': is_planet,
                'is_star': is_star
    })
