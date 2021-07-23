from django import urls
from django.urls import path
from django.urls.conf import include

# this imports all the methods from the views file
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'blogs', views.BlogView)

urlpatterns = [
    path('', views.index, name='index'),
    path('view',views.view_data, name='viewdata'),
    path('api/v1/',include(router.urls))
]