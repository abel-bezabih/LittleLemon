from django.shortcuts import render
from rest_framework import generics, permissions
from .models import MenuItem, Order
from .serializers import MenuItemSerializer, OrderSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['price', 'inventory']
    ordering_fields = ['price', 'title']
    search_fields = ['title']

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAdminUser()]
        return super().get_permissions()

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class AddManagerView(generics.CreateAPIView):
    def post(self, request):
        user = User.objects.get(id=request.data["user_id"])
        group = Group.objects.get(name="Manager")
        user.groups.add(group)
        return Response({"message": "User added to Manager group"}, status=201)

class OrderListView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name="Manager").exists():
            return Order.objects.all()
        return Order.objects.filter(customer=user)

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
