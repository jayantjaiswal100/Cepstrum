from django.urls import path
from . import views
app_name='dp'
urlpatterns = [
    path('', views.DonationCreateView.as_view(), name='all'),
    path('list', views.DonationList.as_view(), name='list'),
    path('confirmation/<pk>', views.DonationDetailView.as_view() ,name='pay'),
]
