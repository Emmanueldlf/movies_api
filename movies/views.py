from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import MovieData
from django.views.generic.list import ListView
from django.core.paginator import Paginator

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

def list(request):
    movie_objects = MovieData.objects.all()
    paginator = Paginator(movie_objects,4)
    page = request.GET.get('page')
    movie_objects = paginator.get_page(page)

    return render(request,'movies/movies_list.html',{'movie_objects':movie_objects})

class MoviesClassView(ListView):
    model = MovieData
    template_name = 'movies/movies_list.html'
    context_object_name = 'movie_objects'
