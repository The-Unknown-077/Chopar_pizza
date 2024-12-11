from rest_framework import serializers
import re
from .models import Product, Cart, CartItem, Customer, Payment , Pizza , Order ,Customer , DeliveryPerson, User








class PizzaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pizza
        fields = '__all__'   
        
        
 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'birth_date', 'birth_year']

    def validate_phone_number(self, value):
        phone_regex = re.compile(r"^\+998[0-9]{9}$")
        if not phone_regex.match(value):
            raise serializers.ValidationError("Неверный формат номера телефона")
        return value

    def validate_birth_date(self, value):
        if value.year > 2024:  # Допустим, не допускаем будущие года
            raise serializers.ValidationError("Дата рождения не может быть в будущем")
        return value


class OrderSerializer(serializers.ModelSerializer):
    pizza = PizzaSerializer(read_only=True)  
    pizza_id = serializers.PrimaryKeyRelatedField(
        queryset=Pizza.objects.all(), source='pizza', write_only=True
    )  

    class Meta:
        model = Order
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'username', 'email', 'phone', 'address']  

class DeliveryPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryPerson
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True) 
    order_id = serializers.PrimaryKeyRelatedField(
        queryset=Order.objects.all(), source='order', write_only=True
    ) 

    class Meta:
        model = Payment
        fields = '__all__'
    
    


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source='product', write_only=True
    )

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_id', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    customer = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'customer', 'items', 'created_at']


