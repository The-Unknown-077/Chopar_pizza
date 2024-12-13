from rest_framework import viewsets
from apps.common.models import Product,ProductPrice,Order,OrderItem,ContactInfo,CustomUser,UserLocation
from apps.common.serializers import ProductSerializer,ProductPriceSerialzier,OrderSerializer,OrderItemSerializer,ContactInfoSerializer,CustomUserSerializer,UserLocationSerialzer
from rest_framework.viewsets import ModelViewSet 
from rest_framework.permissions import IsAuthenticated 


class UnifiedViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        model = self.serializer_class.Meta.model
        return model.objects.all()


class ProductViewSet(UnifiedViewSet):
    serializer_class = ProductSerializer


class ProductPriceViewSet(UnifiedViewSet):
    serializer_class = ProductPriceSerialzier


class OrderViewSet(UnifiedViewSet):
    serializer_class = OrderSerializer


class OrderItemViewSet(UnifiedViewSet):
    serializer_class = OrderItemSerializer


class ContactInfoViewSet(UnifiedViewSet):
    serializer_class = ContactInfoSerializer


class CustomUserViewSet(UnifiedViewSet):
    serializer_class = CustomUserSerializer


class UserLocationViewSet(UnifiedViewSet):
    serializer_class = UserLocationSerialzer
