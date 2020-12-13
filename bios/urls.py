from django.urls import path, reverse_lazy
from . import views

app_name='bios'
urlpatterns = [
    path('', views.BioListView.as_view(), name='all'),
    path('project', views.ProjectListView.as_view(), name='project_list'),
    path('bio/<int:pk>', views.BioDetailView.as_view(), name='bio_detail'),
    path('project/<int:pk>', views.ProjectDetailView.as_view(), name='project_detail'),
    path('bio/create',views.BioCreateView.as_view(success_url=reverse_lazy('bios:all')), name='bio_create'),
    path('bio/<int:pk>/update',views.BioUpdateView.as_view(), name='bio_update'),
    path('bio/<int:pk>/delete',views.BioDeleteView.as_view(), name='bio_delete'),
    path('project/<int:pk>/update',views.ProjectUpdateView.as_view(), name='project_update'),
    path('project/new', views.ProjectCreateView.as_view(), name='project_create'),
    path('intrest', views.IntrestCreateView.as_view(), name='intrest_create'),
    path('techskill', views.TechSkillCreateView.as_view(), name='techskill_create'),
    
]
