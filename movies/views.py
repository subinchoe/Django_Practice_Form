from django.shortcuts import render, redirect, get_object_or_404
from .forms import MovieForm
from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    
    context = {
        'movies': movies,
    }

    return render(request, 'index.html', context)

def create(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()

            return redirect('movies:detail', movie.id)
    else:
        form = MovieForm()
    
    context = {
        'form': form,
    }

    return render(request, 'form.html', context)

def detail(request, id):
    movie = get_object_or_404(Movie, id=id)

    context = {
        'movie': movie,
    }

    return render(request, 'detail.html', context)

def update(request, id):
    movie = get_object_or_404(Movie, id=id)

    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        
        if form.is_valid():
            form.save()

            return redirect('movies:detail', id)

    else:
        form = MovieForm(instance=movie)

    context = {
        'form': form,
    }
    
    return render(request, 'form.html', context)

def delete(request, id):
    movie = get_object_or_404(Movie, id=id)
    
    if request.method == "POST":
        movie.delete()

        return redirect('movies:index')
    else:

        return redirect('movies:detail', id)