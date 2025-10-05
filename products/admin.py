from django.contrib import admin
from .models import Product

# تسجيل نموذج Product في واجهة الإدارة
# هذا يسمح بإدارة المنتجات من خلال لوحة التحكم
admin.site.register(Product)
