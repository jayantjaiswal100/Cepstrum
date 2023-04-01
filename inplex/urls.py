from django.urls import path, reverse_lazy
from . import views

app_name='inplex'
urlpatterns = [
    path('', views.HomeView.as_view(), name='all'),
    #  path('<int:pk>', views.StudentDetailView.as_view(), name='detail'),
    path('create',views.StudentCreateView.as_view(success_url=reverse_lazy('inplex:all')), name='student_create'),
    path('create_experience',views.ExperienceCreateView.as_view(success_url=reverse_lazy('inplex:all')), name='experience_create'),
    path('experience', views.experience, name='experience'),
    # path('experienceprofile', views.experienceprofile, name='experienceprofile'),
	path("<int:owner_id>", views.experienceprofile, name ="experienceprofile"),


    #  path('bio/<int:pk>/update',views.AlumniUpdateView.as_view(), name='alumni_update'),
    #  path('bio/<int:pk>', views.AlumniDetailView.as_view(), name='alumni_detail'),
]
