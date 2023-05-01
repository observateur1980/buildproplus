from . import views
from django.urls import path

app_name = 'home'
urlpatterns = [


    path('', views.Home.as_view(), name='home'),
    path('projectpage', views.ProjectPage.as_view(), name='projectpage'),
    path('newproject', views.CreateProject.as_view(), name='newproject'),


]
