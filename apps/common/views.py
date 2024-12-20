from rest_framework import generics
from apps.common import models, serializers
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from .models import Order, OrderItem, ProductPrice
from apps.common.serializers import ProductSerializer,ProductPriceSerialzier,OrderSerializer,OrderItemSerializer,ContactInfoSerializer,CustomUserSerializer,UserLocationSerialzer,CartSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.http import JsonResponse
# from rest_framework_simplejwt.tokens import RefreshToken
import random
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model



class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer



class ProductPriceListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.ProductPrice.objects.all()
    serializer_class = serializers.ProductPriceSerialzier  


class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


class OrderItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.OrderItem.objects.all()
    serializer_class = serializers.OrderItemSerializer


class ContactInfoListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.ContactInfo.objects.all()
    serializer_class = serializers.ContactInfoSerializer



# class CustomUserListCreateAPIView(generics.ListCreateAPIView):
#     queryset = models.CustomUser.objects.all()
#     serializer_class = serializers.CustomUserSerializer




class UserLocationListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.UserLocation.objects.all()
    serializer_class = serializers.UserLocationSerialzer 
    
    
    
class CartListCreateView(generics.ListCreateAPIView):
   
    queryset = Order.objects.filter(status='PENDING')
    serializer_class = CartSerializer

    def create(self, request, *args, **kwargs):
      
        product_price_id = request.data.get('product_price')
        quantity = request.data.get('quantity', 1)

       
        order, created = Order.objects.get_or_create(
            customer_name=request.data.get('customer_name'),
            customer_phone=request.data.get('customer_phone'),
            address=request.data.get('address'),
            status='PENDING',
            defaults={'total_amount': 0}
        )

        product_price = get_object_or_404(ProductPrice, id=product_price_id)

       
        order_item, item_created = OrderItem.objects.get_or_create(
            order=order,
            product_price=product_price,
            defaults={'quantity': quantity}
        )

        if not item_created:
            
            order_item.quantity += int(quantity)
            order_item.save()

        # Update the total amount of the order
        order.total_amount += product_price.price * int(quantity)
        order.save()

        return Response(CartSerializer(order).data, status=status.HTTP_201_CREATED)


class CartItemDeleteView(APIView):
    """
    Delete an item from the cart.
    """
    def delete(self, request, *args, **kwargs):
        order_item_id = kwargs.get('pk')
        order_item = get_object_or_404(OrderItem, id=order_item_id)

        # Update the total amount of the order
        order = order_item.order
        order.total_amount -= order_item.product_price.price * order_item.quantity
        order.save()

        # Delete the item
        order_item.delete()

        return Response({'detail': 'Item removed from cart'}, status=status.HTTP_204_NO_CONTENT)

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import CustomUser, UserLocation
from .serializers import CustomUserSerializer, UserLocationSerializer

# CustomUser uchun ViewSet
class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]  # Faqat adminlar ko'rish/o'zgartirish huquqiga ega

# UserLocation uchun ViewSet
class UserLocationViewSet(viewsets.ModelViewSet):
    queryset = UserLocation.objects.select_related('user').all()
    serializer_class = UserLocationSerializer
    permission_classes = [IsAuthenticated]  # Faqat tizimga kirgan foydalanuvchilar
    lookup_field = 'id'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Foydalanuvchi avtomatik qo'shiladi

# class UserProfile(APIView):

#     def get(self, request):
#         user: User = request.user
#         if not user.is_authenticated:
#             return Response(status=401)
#         data = {
#             'full_name': user.first_name,
#             'phone_number': user.email, 
#         }

#         return Response(data=data)




# User = get_user_model()

# class VerifyEmailView(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         code = request.data.get('verification_code')

#         try:
#             user = User.objects.get(email=email)
#             if user.verification_code == int(code):
#                 user.is_active = True
#                 user.verification_code = None  # Kodni olib tashlaymiz
#                 user.save()
#                 return Response({"detail": "Email tasdiqlandi, endi tizimga kiring."}, status=status.HTTP_200_OK)
#             return Response({"detail": "Noto'g'ri tasdiqlash kodi."}, status=status.HTTP_400_BAD_REQUEST)
#         except User.DoesNotExist:
#             return Response({"detail": "Bunday foydalanuvchi mavjud emas."}, status=status.HTTP_404_NOT_FOUND)


