from rest_framework import serializers
from . import models
from rest_framework import serializers
from apps.common.models import Product, ProductPrice, Order, OrderItem, ContactInfo, CustomUser, UserLocation
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
import random




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
        

# User = get_user_model()

# class RegistrationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['email', 'password']
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         user.is_active = False  # Tasdiqlashdan o'tmaguncha faollashtirmaymiz
#         user.save()

#         # Tasdiqlash kodi yaratish va email yuborish
#         verification_code = random.randint(100000, 999999)
#         user.verification_code = verification_code
#         user.save()

#         send_mail(
#             'Email tasdiqlash kodingiz',
#             f'Tasdiqlash kodingiz: {verification_code}',
#             'noreply@example.com',
#             [user.email],
#         )
#         return user        
        
        
class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product_price', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True, source='orderitem_set')

    class Meta:
        model = Order
        fields = ['id', 'customer_name', 'customer_phone', 'address', 'status', 'created_at', 'total_amount', 'items'] 
        
       