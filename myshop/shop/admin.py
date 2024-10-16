from django.contrib import admin
from .models import Products, Cart


# Register your models here.




@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "count")
    ordering = ("name", "description", "count")

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("product_id", "user", "count", "status")
    ordering = ("product_id", "user", "count", "status")