from django.urls import path,include
from . import views


urlpatterns = [

    path('/planets',views.all_planets, name='planets'),
    path('/stars', views.all_stars, name='stars'),
    path('/planets/<int:pk>',
         views.planet, name='planet_detail'),
    path('/stars/<int:pk>',
         views.star, name='star_detail')
]
