from rest_framework import serializers
from . import models
from rest_framework import serializers
from apps.common.models import Product, ProductPrice, Order, OrderItem, ContactInfo, CustomUser, UserLocation





class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Product
        fields = "__all__"
        
        
class ProductPriceSerialzier(serializers.ModelSerializer):
    class Meta:
        model = models.ProductPrice
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
        fields = '__all__' 
        
       