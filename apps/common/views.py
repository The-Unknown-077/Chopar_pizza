<<<<<<< HEAD
from .models import Pizza, Order, Customer, DeliveryPerson, Payment , Cart , CartItem
from rest_framework import generics , status
from rest_framework.response import Response
from .serializers import (
    PizzaSerializer,
    OrderSerializer,
    CustomerSerializer,
    DeliveryPersonSerializer,
    PaymentSerializer,
    ProductSerializer, CartSerializer, CartItemSerializer, PaymentSerializer

)



class PizzaListCreateView(generics.ListCreateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class PizzaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer



class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class DeliveryPersonListCreateView(generics.ListCreateAPIView):
    queryset = DeliveryPerson.objects.all()
    serializer_class = DeliveryPersonSerializer


class DeliveryPersonRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeliveryPerson.objects.all()
    serializer_class = DeliveryPersonSerializer


class PaymentListCreateView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    
    
    
    
class CartRetrieveView(generics.RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_object(self):
        
        return Cart.objects.get(customer=self.request.user.customer)


class CartItemAddView(generics.CreateAPIView):
    serializer_class = CartItemSerializer

    def create(self, request, *args, **kwargs):
        cart, _ = Cart.objects.get_or_create(customer=request.user.customer)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(cart=cart)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CartItemDeleteView(generics.DestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def get_queryset(self):
        cart = Cart.objects.get(customer=self.request.user.customer)
        return self.queryset.filter(cart=cart)

class PaymentCreateView(generics.CreateAPIView):
    serializer_class = PaymentSerializer

    def create(self, request, *args, **kwargs):
      
        cart = Cart.objects.get(customer=request.user.customer)
        total = sum(item.product.price * item.quantity for item in cart.items.all())

        payment_data = request.data
        payment_data['amount'] = total 
        serializer = self.get_serializer(data=payment_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        cart.items.all().delete()  
        return Response(serializer.data, status=status.HTTP_201_CREATED)
=======
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect  # Shablonlarni render qilish va yo'naltirish uchun
from django.http import HttpResponse  # Javob yaratish uchun
from django.contrib import messages  # Foydalanuvchi uchun xabarlar qo'shish
from .models import CustomUser  # CustomUser modelini import qilish
from .models import RegistrationForm  # RegistrationForm formasini import qilish


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tasdiqlash kodi emailga yuborildi.")
            return redirect('confirm')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def confirm(request):
    if request.method == "POST":
        email = request.POST.get('email')
        confirmation_code = request.POST.get('confirmation_code')
        try:
            user = CustomUser.objects.get(email=email, confirmation_code=confirmation_code)
            user.is_confirmed = True
            user.save()
            messages.success(request, "Tasdiqlash muvaffaqiyatli amalga oshirildi.")
            return redirect('success')
        except CustomUser.DoesNotExist:
            messages.error(request, "Notogri email yoki tasdiqlash kodi.")
    return render(request, 'confirm.html')

def success(request):
    return HttpResponse("Registratsiya muvaffaqiyatli yakunlandi!")

>>>>>>> 9c84f4fb8c8e3fb5acfb5b7dca2dad3dfe3beb05
