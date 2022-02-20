from django.urls import path, reverse_lazy
from . import views

app_name='inplace'
urlpatterns = [
      path('', views.InplaceListView.as_view(), name='all'),
      path('<int:pk>', views.PostDetailView.as_view(), name='detail'),
    
]
