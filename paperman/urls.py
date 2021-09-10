from django.urls import path, reverse_lazy
from . import views

app_name='paperman'
urlpatterns = [
      path('', views.PaperManListView.as_view(), name='all'),
      path('api', views.PaperManList.as_view()),
    
]
