from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Bo'lim nomi")
    description = models.TextField(blank=True, null=True, verbose_name="Bo'lim haqida ma’lumot")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Bo'lim"
        verbose_name_plural = "Bo'limlar"


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", verbose_name="Bo'lim")
    name = models.CharField(max_length=150, verbose_name="Mahsulot nomi")
    description = models.TextField(blank=True, null=True, verbose_name="Mahsulot tavsifi")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narxi")
    year = models.PositiveIntegerField(verbose_name="Ishlab chiqarilgan yil")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan sana")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"


class Customer(models.Model):
    full_name = models.CharField(max_length=150, verbose_name="To'liq ism")
    phone = models.CharField(max_length=20, verbose_name="Telefon raqam")
    email = models.EmailField(blank=True, null=True, verbose_name="Elektron pochta")
    address = models.CharField(max_length=255, verbose_name="Manzil")
    joined_date = models.DateTimeField(auto_now_add=True, verbose_name="Ro'yxatdan o'tgan sana")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders", verbose_name="Buyurtmachi")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="orders", verbose_name="Mahsulot")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Soni")
    total_price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Jami narx")
    order_date = models.DateTimeField(auto_now_add=True, verbose_name="Buyurtma sanasi")
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Kutilmoqda'),
            ('shipped', 'Yetkazilmoqda'),
            ('delivered', 'Yetkazilgan'),
        ],
        default='pending',
        verbose_name="Holati"
    )

    def __str__(self):
        return f"{self.customer.full_name} - {self.product.name}"

    class Meta:
        verbose_name = "Buyurtma"
        verbose_name_plural = "Buyurtmalar"
