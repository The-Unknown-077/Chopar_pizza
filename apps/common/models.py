from django.db import models
from django import forms
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
import random



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





#son generatsiya qlshga
def generate_confirmation_code():
    return str(random.randint(100000, 999999))

class CustomUser(models.Model):
    email = models.EmailField(unique=True)
    confirmation_code = models.CharField(max_length=6, blank=True)
    is_confirmed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.pk:  # Yangi foydalanuvchi uchun tasdiqlash kodi yaratish
            self.confirmation_code = generate_confirmation_code()
        super().save(*args, **kwargs)


#Form
class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            send_confirmation_email(user)
        return user




# Emailli tastiqlash uchunnn
def send_confirmation_email(user):
    subject = "Tasdiqlash kodi"
    message = f"Hurmatli foydalanuvchi, sizning tasdiqlash kodingiz: {user.confirmation_code}"
    from_email = "noreply@example.com"
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list)







