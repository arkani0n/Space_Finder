from django.urls import path,include
from . import views


urlpatterns = [

    path('/planets',views.PlanetListView.as_view(), name='planets'),
    path('/stars', views.StarListView.as_view(), name='stars'),
    path('/planet/<int:pk>',
         views.PlanetDetailView.as_view(), name='planet_detail'),
    path('/star/<int:pk>',
         views.StarDetailView.as_view(), name='star_detail'),
    path('',views.CreateView.as_view())
]
