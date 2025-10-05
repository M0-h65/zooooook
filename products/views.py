from django.shortcuts import render
from .models import Product

# عرض product_list
# هذا العرض يقوم بجلب جميع المنتجات من قاعدة البيانات
# ويمررها إلى القالب لعرضها
def product_list(request):
    # جلب جميع المنتجات
    products = Product.objects.all()
    # تمرير المنتجات إلى القالب
    return render(request, 'products/product_list.html', {'products': products})
