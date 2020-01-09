from django.contrib import admin
from .models import  Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','price', 'updated', 'is_active']
    list_filter = ['price', 'is_active','title']
    list_editable = ['price','is_active']
    search_fields = ['title']





admin.site.register(Product, ProductAdmin)




