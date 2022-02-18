from django.urls import path
from . import views
app_name='timetable'
urlpatterns = [
    path('',views.index, name="index"),
    path('showtable',views.showtable, name="showtable"),
    path('adminpanel',views.TimetableAdminView.as_view(), name="adminpanel"),
    path('submit',views.submit, name="submit"),
    # path('login', views.login, name="login"),
    # path('logout', views.logout, name="logout"),
]
