from django.contrib import admin

# Register your models here.
from .models import Product


class admin_manager(admin.ModelAdmin):
    list_display = ['__str__','slug','product_exist']
    list_filter = ('product_exist',)
    __module__ = Product


admin.site.register(Product,admin_manager)
