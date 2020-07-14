from django.urls import path

from api import views

urlpatterns = [
    path('convert_base', views.des_convert_base, name='convert_base')
]