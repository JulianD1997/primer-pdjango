from django.shortcuts import render
from django.http import HttpResponse
from .models import Director,Gender,Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all().count()
    directors = Director.objects.all().count()
    return HttpResponse(f"Hello,world peliculas{movies}, directores {directors}")
