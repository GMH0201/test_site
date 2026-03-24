# test_dj/urls.py

from django.urls import path
from . import views

app_name = "test_dj"
urlpatterns = [
    path('index/', views.index, name='index'),
]