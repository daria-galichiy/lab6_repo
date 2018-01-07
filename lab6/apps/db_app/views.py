from django.shortcuts import render
from django.views.generic import ListView
from lab6.apps.db_app.models import Actors, Filmmakers, Film_writers, Producers, Cameramen, Countries, Films

# Create your views here.


def main(request):
    return render(request, 'main_page.html')


class CountriesList(ListView):
    model = Countries
    template_name = "countries.html"


class ActorsList(ListView):
    model = Actors
    template_name = "actors.html"


class FilmmakersList(ListView):
    model = Filmmakers
    template_name = "filmmakers.html"


class Film_writersList(ListView):
    model = Film_writers
    template_name = "film_writers.html"


class ProducersList(ListView):
    model = Producers
    template_name = "producers.html"


class CameramenList(ListView):
    model = Cameramen
    template_name = "cameramen.html"


class FilmsList(ListView):
    model = Films
    template_name = "films.html"
