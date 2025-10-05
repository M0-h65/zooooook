from django.db import models

# نموذج Product لتمثيل منتجات الدعاية والإعلان
# هذا النموذج يحتوي على الحقول الأساسية للمنتج
class Product(models.Model):
    # اسم المنتج، حقل نصي قصير
    name = models.CharField(max_length=100)
    # وصف المنتج، حقل نصي طويل
    description = models.TextField()
    # سعر المنتج، حقل رقم عشري
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # تاريخ الإنشاء، يتم تعيينه تلقائيًا عند إنشاء السجل
    created_at = models.DateTimeField(auto_now_add=True)

    # دالة __str__ لعرض اسم المنتج في واجهة الإدارة
    def __str__(self):
        return self.name
