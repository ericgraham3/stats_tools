"""Define URL patterns for stats tools."""
from django.urls import path

from . import views

app_name = 'stats_tools'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('random_sample/', views.random_sample, name='random_sample'),
]
