from django.urls import path, reverse_lazy
from . import views

app_name='inphase'
urlpatterns = [
      path('', views.InphaseListView.as_view(), name='all'),
    
]
