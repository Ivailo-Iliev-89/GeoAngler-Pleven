from django.shortcuts import render, get_object_or_404
from .models import FishingPlace, Method, Fish

# Must change the all def with class based-views , for more practice
# from django.views.generic import ListView,DetailView, DeleteView, UpdateView, CreateView


# The home page
def index(request):
    places = FishingPlace.objects.all()
    return render(request, 'fishing_app/index.html', {'places': places})

# Detail for current location( for example - Vit River)


def place_detail(request, slug):
    place = get_object_or_404(FishingPlace, slug=slug)
    return render(request, 'fishing_app/place_detail.html', {'place': place})

# Filter by methods of fishing


def method_detail(request, slug):
    method = get_object_or_404(Method, slug=slug)
    places = method.places.all()
    return render(request, 'fishing_app/method_filter.html', {
        'method': method,
        'places': places
    })

# Filter by types of locations


def type_filter(request, place_type):
    places = FishingPlace.objects.filter(place_type=place_type)
    type_name = dict(FishingPlace.PLACE_TYPES).get(place_type)
    return render(request, 'fishing_app/type_filter.html', {
        'places': places,
        'type_name': type_name
    })


def about(request):
    return render(request, 'fishing_app/about.html')


def advices(request):
    return render(request, 'fishing_app/advices.html')
