from rest_framework import serializers
from . import models




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
        fields = ('email','confirmation_code','username')

class UserLocationSerialzer(serializers.ModelSerializer):
    model = models.UserLocation
    fields = '__all__' 
    
       