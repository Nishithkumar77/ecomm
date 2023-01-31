from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Category)
admin.site.register(Coupon)

class ProductImageAdmin(admin.StackedInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'price']
    inlines = [ProductImageAdmin]

@admin.register(ColorVariant)
class ColorVariant(admin.ModelAdmin):
    model = ColorVariant
    list_display = ['color_name', 'price']

@admin.register(SizeVariant)
class SizeVariant(admin.ModelAdmin):
    list_display = ['size_name', 'price']
    model = SizeVariant

admin.site.register(Product, ProductAdmin)

admin.site.register(ProductImage)
