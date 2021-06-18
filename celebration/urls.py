from django.urls import path, reverse_lazy
from . import views

app_name='celebration'
urlpatterns = [
      path('', views.CelebrationListView.as_view(), name='all'),
      path('<int:pk>/', views.CelebrationDetailView.as_view(), name='celebration_detail'),
    
]
