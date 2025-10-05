from django.urls import path
from . import views

# URLs لتطبيق products
# هذا الملف يحدد مسارات التطبيق
urlpatterns = [
    # مسار لعرض قائمة المنتجات
    path('', views.product_list, name='product_list'),
]