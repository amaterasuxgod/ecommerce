from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.


class OrderSpecificationInline(admin.TabularInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
       OrderSpecificationInline,
    ]