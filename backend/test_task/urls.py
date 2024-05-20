from django.urls import path

from . import views

app_name = 'test_task'

urlpatterns = [
    path('', views.index),
    path('get/', views.get_response),
]