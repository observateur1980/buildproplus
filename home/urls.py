from . import views
from django.urls import path

app_name = 'home'
urlpatterns = [


    path('', views.Home.as_view(), name='home'),
    path('projectpage', views.ProjectPage.as_view(), name='projectpage'),
    path('create-project', views.create_project, name='create-project'),



]
