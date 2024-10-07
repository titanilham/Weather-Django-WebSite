
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Убедитесь, что здесь только index
]