import uuid
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.utils.text import slugify
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string

from blog.forms import ReportPostForm
from blog.models import Post
from .models import FishingPlace, Method
from .utils import get_weather_data, get_danube_levels


# Начална страница с галерия за нерегистрирани / пренасочва логнати потребители
def index(request):
    if request.user.is_authenticated:
        return redirect('discover')

    landing_locations = [
        {'name': 'р. Вит (гр. Гулянци)', 'img': 'images/vit.jpg'},
        {'name': 'гр. Никопол', 'img': 'images/nikopol.jpg'},
        {'name': 'с. Байкал', 'img': 'images/baikal.jpg'},
        {'name': 'с. Загражден', 'img': 'images/zagrajden.jpg'},
        {'name': 'гр. Белене', 'img': 'images/belene.jpg'},
        {'name': 'Устие на р. Искър', 'img': 'images/iskar.html'},
    ]
    return render(request, 'fishing_app/index.html', {'locations': landing_locations})


# Детайлна страница за водоем с прогноза за времето, репортажи и форма за нов репортаж
@login_required
def place_detail(request, slug):
    place = get_object_or_404(FishingPlace, slug=slug)
    weather = None

    if place.latitude and place.longitude:
        weather = get_weather_data(place.latitude, place.longitude)

    posts = place.posts.filter(status='1').order_by('-created_on')
    total_reports = posts.count()
    last_activity = posts.first().created_on if total_reports > 0 else None

    if request.method == 'POST':
        form = ReportPostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.location = place
            new_post.author = request.user
            new_post.status = '1'

            generated_slug = slugify(new_post.title)
            if not generated_slug:
                new_post.slug = slugify(f"report-{uuid.uuid4().hex[:8]}")
            else:
                new_post.slug = f"{generated_slug}-{uuid.uuid4().hex[:4]}"

            new_post.save()
            return redirect('place_detail', slug=slug)
    else:
        form = ReportPostForm()

    return render(request, 'fishing_app/place_detail.html', {
        'place': place,
        'posts': posts,
        'form': form,
        'weather': weather,
        'total_reports': total_reports,
        'last_activity': last_activity,
    })


# Филтриране на водоеми по конкретен метод на риболов (напр. фидер, спининг)
@login_required
def method_detail(request, slug):
    method = get_object_or_404(Method, slug=slug)
    places = method.places.all()
    return render(request, 'fishing_app/method_filter.html', {
        'method': method,
        'places': places
    })


# Филтриране на местата по тип на водоема (река, язовир)
@login_required
def type_filter(request, place_type):
    places = FishingPlace.objects.filter(place_type=place_type)
    type_name = dict(FishingPlace.PLACE_TYPES).get(place_type)
    return render(request, 'fishing_app/type_filter.html', {
        'places': places,
        'type_name': type_name
    })


# Статична страница "За нас" във футъра на сайта
def about(request):
    return render(request, 'fishing_app/about.html')


# Статична страница с риболовни съвети и тактики във футъра
def advices(request):
    return render(request, 'fishing_app/advices.html')


# Регистрация на нов потребител с автоматично вписване в системата
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})


# Основно табло за логнати потребители с препоръчани места и статистика на кълването
@login_required
def discover(request):
    recommended_places = FishingPlace.objects.filter(is_recommended=True)[:5]
    total_posts = Post.objects.filter(status='1').count()

    if total_posts > 0:
        active_count = Post.objects.filter(
            status='1', bite_status='active').count()
        weak_count = Post.objects.filter(
            status='1', bite_status='weak').count()
        capo_count = Post.objects.filter(
            status='1', bite_status='capo').count()

        reports_stats = {
            'active': int((active_count / total_posts) * 100),
            'weak': int((weak_count / total_posts) * 100),
            'capo': int((capo_count / total_posts) * 100),
        }
    else:
        reports_stats = {'active': 0, 'weak': 0, 'capo': 0}

    context = {
        'recommended': recommended_places,
        'stats': reports_stats,
    }
    return render(request, 'fishing_app/discover.html', context)


# Филтриране на водоеми според активността на рибата (кълве, слабо, капо)
@login_required
def bite_filter_view(request, status_type):
    places = FishingPlace.objects.filter(
        posts__bite_status=status_type,
        posts__status='1'
    ).distinct()

    titles = {
        'active': 'Водоеми, на които в момента КЪЛВЕ',
        'weak': 'Водоеми със слаба активност',
        'capo': '❌ Водоеми, на които колегите са КАПО',
    }

    context = {
        'places': places,
        'title': titles.get(status_type, "Риболовна активност"),
    }

    return render(request, 'fishing_app/access_results.html', context)


# Страница за следене на хидрологичните нива на река Дунав по станции
@login_required
def river_levels_view(request):
    danube_data = get_danube_levels()
    return render(request, 'fishing_app/river_levels.html', {'danube_stations': danube_data})


# Филтриране на водоемите по тип достъп – свободни (с билет) или платени (с такса)
@login_required
def access_filter_view(request, access_type):
    filtered_places = FishingPlace.objects.filter(access_type=access_type)
    title = "Свободни водоеми (с билет)" if access_type == 'free' else "Платени обекти (такса)"

    context = {
        'places': filtered_places,
        'title': title,
    }
    return render(request, 'fishing_app/access_results.html', context)


# Търсачка за водоеми по име, описание, видове риба или методи за риболов
@login_required
def search_results(request):
    query = request.GET.get('q', '').strip()
    results = []

    if query:
        results = FishingPlace.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(fishes__name__icontains=query) |
            Q(methods__name__icontains=query)
        ).distinct()

    return render(request, 'fishing_app/search_results.html', {
        'results': results,
        'query': query
    })


# Личен потребителски профил, показващ собствените излети на потребителя
@login_required
def user_profile(request):
    my_posts = Post.objects.filter(
        author=request.user, status='1').order_by('-created_on')
    my_reports_count = my_posts.count()

    return render(request, 'registration/profile.html', {
        'my_posts': my_posts,
        'my_reports_count': my_reports_count
    })
