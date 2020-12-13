from django.urls import path, reverse_lazy
from . import views

app_name='alumni'
urlpatterns = [
     path('', views.AlumniListView.as_view(), name='all'),
     path('bio/<int:pk>', views.AlumniDetailView.as_view(), name='alumni_detail'),
     path('bio/create',views.AlumniCreateView.as_view(success_url=reverse_lazy('alumni:all')), name='alumni_create'),
     path('bio/<int:pk>/update',views.AlumniUpdateView.as_view(), name='alumni_update'),
     path('bio/<int:pk>', views.AlumniDetailView.as_view(), name='alumni_detail'),
]
