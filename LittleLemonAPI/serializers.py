from rest_framework import serializers
from .models import Category, MenuItem, Cart, Order, OrderItem
from django.contrib.auth.models import User
from datetime import datetime



class UserSerializer(serializers.ModelSerializer):
    Date_Joined = serializers.SerializerMethodField()
    date_joined = serializers.DateTimeField(write_only=True, default=datetime.now)
    email = serializers.EmailField(required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_joined', 'Date_Joined']

    def get_Date_Joined(self, obj):
        return obj.date_joined.strftime('%Y-%m-%d')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class MenuItemSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'featured', 'category', 'category_id']
        depth = 1


class CartHelpSerializer(serializers.ModelSerializer):
    class Meta():
        model = MenuItem
        fields = ['id', 'title', 'price']


class CartSerializer(serializers.ModelSerializer):
    menuitem = CartHelpSerializer()

    class Meta():
        model = Cart
        fields = ['menuitem', 'quantity', 'price']


class AddToCartSerializer(serializers.ModelSerializer):
    class Meta():
        model = Cart
        fields = ['menuitem', 'quantity']


class RemoveFromCartSerializer(serializers.ModelSerializer):
    class Meta():
        model = Cart
        fields = ['menuitem']

class OrdersSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta():
        model = Order
        fields = ['id','user','total','status','delivery_crew','date']

class SingleHelperSerializer(serializers.ModelSerializer):
    class Meta():
        model = MenuItem
        fields = ['title','price']

class SingleOrderSerializer(serializers.ModelSerializer):
    menuitem = SingleHelperSerializer()
    class Meta():
        model = OrderItem
        fields = ['menuitem','quantity']
    unit_price = serializers.DecimalField(max_digits=6, decimal_places=2, source='menuitem.price', read_only=True)
    price = serializers.DecimalField(max_digits=6, decimal_places=2, read_only=True)
    name = serializers.CharField(source='menuitem.title', read_only=True)

    class Meta:
        model = OrderItem
        fields = ['name', 'quantity', 'unit_price', 'price', 'menuitem']
        extra_kwargs = {
            'menuitem': {'read_only': True}
        }

class OrderPutSerializer(serializers.ModelSerializer):
    class Meta():
        model = Order
        fields = ['delivery_crew']

class OrderItemSerializer(serializers.ModelSerializer):
    # order = UserSerializer(read_only=True)
    user_id = serializers.IntegerField()
    menuitem = MenuItemSerializer(read_only=True)
    menuitem_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = OrderItem
        fields = ['user_id', 'menuitem', 'menuitem_id', 'quantity', 'unit_price', 'price']


class OrderSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    orderitem = OrderItemSerializer(read_only=True)
    orderitem_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user_id', 'delivery_crew', 'status', 'total', 'date', 'orderitem', 'orderitem_id', ]
