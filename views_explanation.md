# شرح عرض product_list (views.py)

```python
from django.shortcuts import render  # استيراد دالة render من django.shortcuts لعرض القوالب
from .models import Product  # استيراد نموذج Product من نفس التطبيق

# تعريف دالة product_list التي تتعامل مع طلب عرض قائمة المنتجات
def product_list(request):
    # جلب جميع كائنات Product من قاعدة البيانات باستخدام Product.objects.all()
    products = Product.objects.all()
    # إرجاع استجابة HTTP باستخدام render، تمرير الطلب، مسار القالب، والسياق
    return render(request, 'products/product_list.html', {'products': products})
```

## شرح مفصل:
- **from django.shortcuts import render**: استيراد دالة render التي تستخدم لعرض القوالب مع السياق.
- **from .models import Product**: استيراد نموذج Product للوصول إلى البيانات.
- **def product_list(request)**: تعريف دالة العرض التي تأخذ معامل request (كائن الطلب HTTP).
- **products = Product.objects.all()**: استعلام لجلب جميع المنتجات من قاعدة البيانات.
- **return render(request, 'products/product_list.html', {'products': products})**: إرجاع صفحة HTML مع تمرير قائمة المنتجات كسياق.