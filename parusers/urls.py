from django.urls import path
from . import views

app_name = 'parusers'
urlpatterns = [

    path('logout', views.user_logout, name='logout'),

]
