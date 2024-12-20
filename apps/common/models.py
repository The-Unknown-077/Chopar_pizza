from django.db import models
from django import forms
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.models import AbstractUser
import random
from django.contrib.auth.hashers import make_password
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin




class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.name


class ProductPrice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    size = models.CharField(max_length=200)




    






class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=15)  
    address = models.TextField() 
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')  
    created_at = models.DateTimeField(auto_now_add=True)  
    total_amount = models.IntegerField()

    def __str__(self):
        return f"{self.customer_name} - {self.pizza.name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_price = models.ForeignKey(ProductPrice, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)






class ContactInfo(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField()
    order_id = models.IntegerField()  
    comment = models.TextField()

    def __str__(self):
        return self.full_name











from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email address is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_active = True  # Foydalanuvchi faol holatda bo'lishi uchun
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError("Superuser must have is_staff=True.")
        if not extra_fields.get('is_superuser'):
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=False, blank=False)
    is_active = models.BooleanField(default=True)  # Default True qilib qo'yildi
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class UserLocation(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="locations"
    )
    latitude = models.FloatField(null=False, blank=False)
    longitude = models.FloatField(null=False, blank=False)  # To'g'ri yozilgan
    home = models.CharField(max_length=200, blank=True)
    kv = models.CharField(max_length=200, blank=True)
    podyezd = models.CharField(max_length=200, blank=True)
    domofon_code = models.CharField(max_length=200, blank=True)
    name_address = models.CharField(max_length=200, blank=True)
    is_active = models.BooleanField(default=True)  # Foydalanuvchi joylashuvi faol

    def __str__(self):
        return f"{self.user.email} - {self.name_address or 'Unnamed Address'}"
