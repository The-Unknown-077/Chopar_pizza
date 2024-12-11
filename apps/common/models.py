from django.db import models



class Pizza(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name
    
    
    






class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=15)  
    address = models.TextField() 
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE) 
    quantity = models.PositiveIntegerField(default=1)  
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')  
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.customer_name} - {self.pizza.name}"




from django.contrib.auth.models import AbstractUser

class Customer(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)  
    address = models.TextField(blank=True, null=True)  

    def __str__(self):
        return self.username








class DeliveryPerson(models.Model):
    name = models.CharField(max_length=100)  
    phone = models.CharField(max_length=15)  
    available = models.BooleanField(default=True)  

    def __str__(self):
        return self.name



class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)  
    amount = models.DecimalField(max_digits=10, decimal_places=2)  
    payment_date = models.DateTimeField(auto_now_add=True)  
    payment_method = models.CharField(max_length=50, choices=[
        ('CASH', 'Cash'),
        ('CARD', 'Card'),
        ('ONLINE', 'Online'),
    ])  

    def __str__(self):
        return f"{self.order.customer_name} - {self.amount}"
    
    
    
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Cart(models.Model):
    customer = models.OneToOneField('Customer', on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart for {self.customer.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"
    
    
    
    

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)  # +998901234567
    email = models.EmailField()
    birth_date = models.DateField()
    birth_year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}
    
    
    
    
 

