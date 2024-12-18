from rest_framework import serializers
from . import models
from rest_framework import serializers
from apps.common.models import Product, ProductPrice, Order, OrderItem, ContactInfo, CustomUser, UserLocation

class ProductPriceSerialzier(serializers.ModelSerializer):
    class Meta:
        model = models.ProductPrice
        fields = "__all__"
        
class ProductSerializer(serializers.ModelSerializer):
    price = ProductPriceSerialzier(many=True,read_only = True,source="ProductPrice")
    class Meta:
        model = models.Product
        fields = "__all__"
        



        

        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = "__all__"
        
        
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItem
        fields = "__all__"
        
        
class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactInfo
        fields = "__all__"
        
        
        
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = "__all__"
class UserLocationSerialzer(serializers.ModelSerializer):
    class Meta:
        model = models.UserLocation
        exclude = ("is_active",)
        
        
        
        
class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product_price', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True, source='orderitem_set')

    class Meta:
        model = Order
        fields = ['id', 'customer_name', 'customer_phone', 'address', 'status', 'created_at', 'total_amount', 'items'] 
        
       