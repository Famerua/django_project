from django.shortcuts import render
from .models import Movie


# Create your views here.
def get_movies(request):
    movies = Movie.objects.all()
    return render(
        request=request, template_name="Movie/index.html", context={"movies": movies}
    )


def get_the_movie(request, pk):
    movie = Movie.objects.get(id=pk)
    return render(
        request=request,
        template_name="Movie/movie_details.html",
        context={"movie": movie},
    )
