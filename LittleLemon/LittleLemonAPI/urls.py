from django.urls import path
from .views import (
    CategoryListView, MenuItemListView, MenuItemDetailView,
    CartListView, CartDetailView, OrderListView, OrderDetailView
)

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('menu-items/', MenuItemListView.as_view(), name='menuitem-list'),
    path('menu-items/<int:pk>/', MenuItemDetailView.as_view(), name='menuitem-detail'),
    path('cart/', CartListView.as_view(), name='cart-list'),
    path('cart/<int:pk>/', CartDetailView.as_view(), name='cart-detail'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
]
