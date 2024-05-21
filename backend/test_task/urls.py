from django.urls import path

from . import views


app_name = 'test_task'

urlpatterns = [
    path('', views.index, name='input_response'),
    path('get/', views.get_response, name='get_result'),
    path('task/', views.get_test_task, name='get_task'),
]
