from django.urls import path
from .views import MenuItemsView, SingleMenuItemView, OrderListView, OrderDetailView, AddManagerView

urlpatterns = [
    path('menu-items/', MenuItemsView.as_view(), name="menu-items"),
    path('menu-items/<int:pk>/', SingleMenuItemView.as_view(), name="single-menu-item"),
    path('orders/', OrderListView.as_view(), name="orders"),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name="order-detail"),
    path('groups/manager/users/', AddManagerView.as_view(), name="add-manager"),
]
