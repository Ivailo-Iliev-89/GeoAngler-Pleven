from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('place/<slug:slug>/', views.place_detail, name='place_detail'),
    path('method/<slug:slug>/', views.method_detail, name='method_detail'),
    path('type/<str:place_type>/', views.type_filter, name='type_filter'),
    path('about/', views.about, name='about'),
    path('advices/', views.advices, name='advices'),
    path('discover/', views.discover, name='discover'),
    path('river-levels/', views.river_levels_view, name='river_levels'),
    path('explore/bite/<str:status_type>/',
         views.bite_filter_view, name='bite_filter'),
    path('explore/access/<str:access_type>/',
         views.access_filter_view, name='access_filter'),
    path('search/', views.search_results, name='search_results'),
    path('profile/', views.user_profile, name='user_profile'),
]
