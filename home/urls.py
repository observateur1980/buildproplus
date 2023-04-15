from . import views
from django.urls import path

app_name = 'home'
urlpatterns = [

    path('', views.Index.as_view(), name='index'),
    path('home', views.Home.as_view(), name='home'),
    path('projectpage', views.ProjectPage.as_view(), name='projectpage'),




]
