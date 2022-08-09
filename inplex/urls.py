from django.urls import path, reverse_lazy
from . import views

app_name='inplex'
urlpatterns = [
    #  path('', views.AlumniListView.as_view(), name='all'),
    #  path('bio/<int:pk>', views.AlumniDetailView.as_view(), name='alumni_detail'),
    path('create',views.StudentCreateView.as_view(success_url=reverse_lazy('inplex:all')), name='student_create'),
    #  path('bio/<int:pk>/update',views.AlumniUpdateView.as_view(), name='alumni_update'),
    #  path('bio/<int:pk>', views.AlumniDetailView.as_view(), name='alumni_detail'),
]
