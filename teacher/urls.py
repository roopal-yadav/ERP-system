from django.urls import path,re_path
from . import views

app_name='teacher'

urlpatterns = [
    path('homepage/', views.index, name='index'),
    path('logout/',views.logout,name='logout'),
    path('login/',views.login,name='login'),
    path('tt/',views.tt,name="timetable"),
    re_path(r'^$',views.index,name="index"),
]
