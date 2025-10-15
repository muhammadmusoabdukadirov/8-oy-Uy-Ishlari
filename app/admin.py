from django.contrib import admin

# Register your models here.
from .models import Category, Product, Customer, Order


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)
    list_per_page = 20
    ordering = ('id',)
    verbose_name = "Bo'lim"
    verbose_name_plural = "Bo'limlar"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'year', 'created_at')
    list_filter = ('category', 'year')
    search_fields = ('name',)
    list_per_page = 20
    ordering = ('id',)
    verbose_name = "Mahsulot"
    verbose_name_plural = "Mahsulotlar"


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone', 'email', 'joined_date')
    search_fields = ('full_name', 'phone', 'email')
    list_per_page = 20
    ordering = ('id',)
    verbose_name = "Foydalanuvchi"
    verbose_name_plural = "Foydalanuvchilar"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'product', 'quantity', 'total_price', 'status', 'order_date')
    list_filter = ('status', 'order_date')
    search_fields = ('customer__full_name', 'product__name')
    list_per_page = 20
    ordering = ('-order_date',)
    verbose_name = "Buyurtma"
    verbose_name_plural = "Buyurtmalar"
