from django.contrib import admin
from .models import (
    Restoran, Menyu, Idish,
    Foydalanuvchi, Buyurtma,
    Haydovchi, YetkazibBerish,
    Tolov, KoribChiqish
)


@admin.register(Restoran)
class RestoranAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'manzil', 'telefon', 'ochilish_vaqti', 'yopilish_vaqti')
    search_fields = ('nom', 'manzil', 'telefon')
    list_per_page = 20
    ordering = ('id',)
    verbose_name = "Restoran"
    verbose_name_plural = "Restoranlar"


@admin.register(Menyu)
class MenyuAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'restoran', 'yaratilgan_vaqt')
    search_fields = ('nom', 'restoran__nom')
    list_filter = ('restoran',)
    list_per_page = 20
    ordering = ('-yaratilgan_vaqt',)
    verbose_name = "Menyu"
    verbose_name_plural = "Menyular"


@admin.register(Idish)
class IdishAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'menyu', 'narx', 'mavjud')
    search_fields = ('nom', 'menyu__nom')
    list_filter = ('mavjud', 'menyu')
    list_per_page = 20
    ordering = ('id',)
    verbose_name = "Idish"
    verbose_name_plural = "Idishlar"


@admin.register(Foydalanuvchi)
class FoydalanuvchiAdmin(admin.ModelAdmin):
    list_display = ('id', 'ism', 'familiya', 'telefon', 'manzil', 'royxatdan_otgan_sana')
    search_fields = ('ism', 'familiya', 'telefon')
    list_per_page = 20
    ordering = ('id',)
    verbose_name = "Foydalanuvchi"
    verbose_name_plural = "Foydalanuvchilar"


@admin.register(Buyurtma)
class BuyurtmaAdmin(admin.ModelAdmin):
    list_display = ('id', 'foydalanuvchi', 'idish', 'miqdor', 'umumiy_narx', 'holat', 'yaratilgan_vaqt')
    search_fields = ('foydalanuvchi__ism', 'idish__nom')
    list_filter = ('holat', 'yaratilgan_vaqt')
    list_per_page = 20
    ordering = ('-yaratilgan_vaqt',)
    verbose_name = "Buyurtma"
    verbose_name_plural = "Buyurtmalar"


@admin.register(Haydovchi)
class HaydovchiAdmin(admin.ModelAdmin):
    list_display = ('id', 'ism', 'familiya', 'telefon', 'transport')
    search_fields = ('ism', 'familiya', 'telefon')
    list_per_page = 20
    ordering = ('id',)
    verbose_name = "Haydovchi"
    verbose_name_plural = "Haydovchilar"


@admin.register(YetkazibBerish)
class YetkazibBerishAdmin(admin.ModelAdmin):
    list_display = ('id', 'buyurtma', 'haydovchi', 'manzil', 'yetkazilgan_vaqt')
    search_fields = ('buyurtma__foydalanuvchi__ism', 'manzil')
    list_filter = ('yetkazilgan_vaqt',)
    list_per_page = 20
    ordering = ('-yetkazilgan_vaqt',)
    verbose_name = "Yetkazib berish"
    verbose_name_plural = "Yetkazib berishlar"



@admin.register(Tolov)
class TolovAdmin(admin.ModelAdmin):
    list_display = ('id', 'buyurtma', 'summa', 'usul', 'tolangan_vaqt')
    search_fields = ('buyurtma__foydalanuvchi__ism',)
    list_filter = ('usul', 'tolangan_vaqt')
    list_per_page = 20
    ordering = ('-tolangan_vaqt',)
    verbose_name = "Tolov"
    verbose_name_plural = "Tolovlar"



@admin.register(KoribChiqish)
class KoribChiqishAdmin(admin.ModelAdmin):
    list_display = ('id', 'foydalanuvchi', 'idish', 'reyting', 'yaratilgan_vaqt')
    search_fields = ('foydalanuvchi__ism', 'idish__nom')
    list_filter = ('reyting',)
    list_per_page = 20
    ordering = ('-yaratilgan_vaqt',)
    verbose_name = "Korib chiqish"
    verbose_name_plural = "Korib chiqishlar"
