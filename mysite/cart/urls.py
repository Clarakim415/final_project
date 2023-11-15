from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('add/<int:coffee_id>/', views.add_cart, name='add_cart'),
    path('', views.cart_detail, name='cart_detail'),
    path('remove/<int:coffee_id>/', views.cart_remove, name='cart_remove'),
    path('full_remove/<int:coffee_id>/', views.full_remove, name='full_remove'),
    path('order-created/<int:order_id>/', views.add_order, name='order-created')
]