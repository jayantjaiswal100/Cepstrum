from django.urls import path, reverse_lazy
from . import views

app_name='inplace'
urlpatterns = [
      path('', views.InplaceListView.as_view(), name='all'),
      path('<int:pk>', views.InplaceDetailView.as_view(), name='detail'),
      path('api', views.PostManList.as_view()),
      path('api/<int:pk>', views.PostRetrive.as_view()),
    
]
