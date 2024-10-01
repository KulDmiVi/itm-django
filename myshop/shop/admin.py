from django.contrib import admin
from shop.models import Clients, Products, Cart


# Register your models here.

@admin.register(Clients)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "phone")
    ordering = ("name", "address", "phone")


@admin.register(Products)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "count")
    ordering = ("name", "description", "count")

@admin.register(Cart)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("product_id", "client_id", "count", "status")
    ordering = ("product_id", "client_id", "count", "status")