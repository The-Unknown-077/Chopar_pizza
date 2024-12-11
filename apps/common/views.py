from rest_framework import generics
from . import models, serializers


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductPriceListCreateView(generics.ListCreateAPIView):
    queryset = models.ProductPrice.objects.all()
    serializer_class = serializers.ProductPriceSerialzier


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


class OrderItemListCreateView(generics.ListCreateAPIView):
    queryset = models.OrderItem.objects.all()
    serializer_class = serializers.OrderItemSerializer

class ContactInfoListCreateView(generics.ListCreateAPIView):
    queryset = models.ContactInfo.objects.all()
    serializer_class = serializers.ContactInfoSerializer

class CustomUserListCreateView(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.CustomUserSerializer


class UserLocationListCreateView(generics.ListCreateAPIView):
    queryset = models.UserLocation.objects.all()
    serializer_class = serializers.UserLocationSerialzer
