from django.urls import path, reverse_lazy
from . import views

app_name='team'
urlpatterns = [
      path('', views.TeamListView.as_view(), name='all'),
      path('prev/<int:pk>', views.PrevTeamListView.as_view(), name='prev'),
      path('api/', views.TeamList.as_view()),
      path('api/<int:pk>', views.TeamRetrive.as_view()),
    
]
