from rest_framework import generics
from apps.common import models, serializers


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



class CustomUserListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.CustomUserSerializer




class UserLocationListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.UserLocation.objects.all()
    serializer_class = serializers.UserLocationSerialzer 
