from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Donation Portal'),
    path('confirmation/', views.homepage ,name='Confirmation'),
]
