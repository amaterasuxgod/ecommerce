from django.contrib import admin
from django import forms
from mptt.admin import MPTTModelAdmin
from .models import Category, Product, ProductImage, ProductSpecification, ProductSpecificationValue, ProductType, Comment

admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Comment)


class ProductSpecificationInline(admin.TabularInline):
    model = ProductSpecification

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    inlines = [
        ProductSpecificationInline,
    ]

class ProductImageInline(admin.TabularInline):
    model = ProductImage

class ProductSpecificationValueInline(admin.TabularInline):
    model = ProductSpecificationValue


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductSpecificationValueInline,
        ProductImageInline,
    ]

