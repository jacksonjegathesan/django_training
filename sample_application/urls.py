from django.urls import path

# this imports all the methods from the views file
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]