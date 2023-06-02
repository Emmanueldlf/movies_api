from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import MovieData
from django.views.generic.list import ListView

# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieSerializer

class ComedyViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(category='comedy')
    serializer_class = MovieSerializer

class ActionViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(category='action')
    serializer_class = MovieSerializer

def movies_list(request):
    movie_objects = MovieData.objects.all()
    return render(request,'movies/movies_list.html',{'movie_objects':movie_objects})

class MoviesClassView(ListView):
    model = MovieData
    template_name = 'movies/movies_list.html'
    context_object_name = 'movie_objects'
