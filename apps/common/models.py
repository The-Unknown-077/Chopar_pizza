from django.db import models
from django import forms
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.models import AbstractUser
import random
from django.contrib.auth.hashers import make_password
from django.contrib.auth.base_user import BaseUserManager





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
        return f"{self.customer_name}"


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










class CustomObject(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)






def generate_confirmation_code():
    return str(random.randint(100000, 999999))

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    confirmation_code = models.CharField(max_length=6, blank=True)
    is_confirmed = models.BooleanField(default=False)

    objects = models.Manager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    username = None

    def save(self, *args, **kwargs):
        if not self.pk:
            self.confirmation_code = generate_confirmation_code()
        super().save(*args, **kwargs)


def send_confirmation_email(user):
    subject = "Tasdiqlash kodi"
    message = f"Hurmatli foydalanuvchi, sizning tasdiqlash kodingiz: {CustomUser.confirmation_code}"
    from_email = "noreply@example.com"
    recipient_list = [CustomUser.email]
    send_mail(subject, message, from_email, recipient_list)



class UserLocation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    latitude = models.FloatField()
    langitude = models.FloatField()
    home = models.CharField(max_length=200)
    kv = models.CharField(max_length=200)
    podyezd = models.CharField(max_length=200)
    domofon_code = models.CharField(max_length=200)
    name_address = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)

