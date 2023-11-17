from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('test/', views.test, name='test'),
    path('test/result/', views.result, name='result'),
    path('', views.index),
    path('mypage/', views.mypage, name='mypage'),
    path('mypage/private_info/', views.mypage, name='mypage'),
    path('mypage/purchase/', views.purchase, name='purchase'),
    path('mypage/subscribe/', views.mypage),
    path('main/popup.html', views.servicePopup),
    path('basket/', views.basket),
    path('add/<int:coffee_id>', views.review_create, name='add'),
    path('review/create/<int:coffee_id>', views.review, name='submit')
]