from django.urls import path, reverse_lazy
from . import views

app_name='inked_intellects'
urlpatterns = [
      path('', views.InkedListView.as_view(), name='all'),
      path('<int:pk>', views.InkedDetailView.as_view(), name='detail'),
    
]
