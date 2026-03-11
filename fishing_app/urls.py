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
    path('search/', views.search_results, name='search_results'),
]
