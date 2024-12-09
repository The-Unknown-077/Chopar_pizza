from django.contrib import admin

from .models import Pizza, Order, Customer, DeliveryPerson, Payment


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')  
    search_fields = ('name',)  



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'pizza', 'status', 'created_at')
    list_filter = ('status',)  
    search_fields = ('customer_name', 'pizza__name')  



@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone', 'address')
    search_fields = ('username', 'email')  




@admin.register(DeliveryPerson)
class DeliveryPersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'available')
    list_filter = ('available',)  



@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'amount', 'payment_date', 'payment_method')
    list_filter = ('payment_method',)  

