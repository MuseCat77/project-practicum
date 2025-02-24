from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.get_fields()]  # Какие поля показывать
    search_fields = ("product", "type")  # Поля для поиска
    list_filter = ("type", "release_date")  # Фильтры сбоку

# Или без декоратора:
# admin.site.register(Product, ProductAdmin)
