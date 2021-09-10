from django.urls import path, reverse_lazy
from . import views

app_name='team'
urlpatterns = [
      path('', views.TeamListView.as_view(), name='all'),
      path('teamapi/', views.TeamList.as_view()),
    
]
