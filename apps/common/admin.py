from django.contrib import admin
from .models import Product,ProductPrice,Order,OrderItem,ContactInfo,CustomUser,UserLocation

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)


@admin.register(ProductPrice)
class ProductPriceAdmin(admin.ModelAdmin):
    list_display = ('product', 'price', 'size')
    search_fields = ('product__name', 'size')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'status', 'total_amount', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('customer_name', 'customer_phone')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product_price', 'quantity')
    search_fields = ('order__customer_name', 'product_price__product__name')


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'order_id')
    search_fields = ('full_name', 'email', 'order_id')


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_confirmed', 'is_staff')
    list_filter = ('is_confirmed', 'is_staff', 'is_superuser')
    search_fields = ('email',)


@admin.register(UserLocation)
class UserLocationAdmin(admin.ModelAdmin):
    list_display = ('user', 'latitude', 'langitude', 'home', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('user__email', 'name_address')
