from .models import Method, FishingPlace
from .utils import get_pleven_weather


def fishing_menu(request):
    return {
        'nav_methods': Method.objects.all(),
        'nav_rivers': FishingPlace.objects.filter(place_type='river'),
        'nav_lakes': FishingPlace.objects.filter(place_type='lake'),
        'nav_swamps': FishingPlace.objects.filter(place_type='swamp'),
    }


def pleven_weather_processor(request):
    weather_data = get_pleven_weather()
    return {
        'pleven_temp': weather_data['temp'],
        'pleven_icon': weather_data['icon']
    }
