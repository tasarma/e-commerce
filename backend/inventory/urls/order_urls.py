from django.urls import path
from inventory.views import order_views as views

urlpatterns = [
    path('create/', views.create_order, name='create_order'),
    path('createItem', views.create_order_item, name='create_order_item'),
    path('getOrderItemNumber/', views.get_order_item_number, name='get_order_item_number'),
    path('getOrderItems/', views.get_order_items, name='get_order_items'),
]
