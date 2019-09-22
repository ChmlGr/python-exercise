from django.urls import path

from . import views

urlpatterns = [
    path('', views.seven_pairs, name='seven_pairs')
]
