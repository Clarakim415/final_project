from django.urls import path
from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index),
    path('mypage/', views.mypage),
    path('signin/', views.signin),
]