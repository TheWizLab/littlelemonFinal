from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from django.shortcuts import get_object_or_404
from . import serializers
from .permissions import IsManager
from django.contrib.auth.models import Group
from django.core.paginator import Paginator, EmptyPage
from datetime import date
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from django.contrib.auth import get_user_model
import json
from . import models
from decimal import Decimal

from . import serializers, models


@throttle_classes([AnonRateThrottle, UserRateThrottle])
class CategoriesView(generics.ListCreateAPIView):
    def get_permissions(self):
        self.permission_classes = []
        if self.request.method != 'GET':
            self.permission_classes = [IsAuthenticated]
        return [permission() for permission in self.permission_classes]
    # def get_queryset(self):
    #     managergroup = self.request.user.groups.filter(name='Manager').exists()
    #     if managergroup:
    #         ;

    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class CategorySingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class MenuItemsView(generics.ListCreateAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = models.MenuItem.objects.all()
    serializer_class = serializers.MenuItemSerializer
    ordering_fields = ['title', 'price', 'featured']
    filterset_fields = ['title', 'price', 'featured']
    search_fields = ['category__icontains']


class MenuItemsSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.MenuItem.objects.all()
    serializer_class = serializers.MenuItemSerializer

class ManagerListView(generics.ListCreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class CartMenu(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.CartSerializer


class OrderListView(generics.ListCreateAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


class GroupListCreate(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.GroupSerializer


class GroupSingle(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.GroupSerializer
