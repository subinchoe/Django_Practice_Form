from django.shortcuts import render, redirect, get_object_or_404
from .forms import MovieForm
from .models import Movie

# Create your views here.
def index(request):
    return render(request, 'index.html')

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

    context={
        'movie': movie,
    }

    return render(request, 'detail.html', context)