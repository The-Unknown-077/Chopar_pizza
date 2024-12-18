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












# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError("Email is required")
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(email, password, **extra_fields)

# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     is_active = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     def __str__(self):
#         return self.email



# class UserLocation(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     latitude = models.FloatField()
#     langitude = models.FloatField()
#     home = models.CharField(max_length=200)
#     kv = models.CharField(max_length=200)
#     podyezd = models.CharField(max_length=200)
#     domofon_code = models.CharField(max_length=200)
#     name_address = models.CharField(max_length=200)
#     is_active = models.BooleanField(default=False)

