from django.urls import path,re_path
from . import views

app_name='teacher'

urlpatterns = [
    path('homepage', views.index, name='index'),
	path('teacher/login/',views.login,name='login'),
    re_path(r'^$',views.index,name="index"),
]
