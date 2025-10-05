# شرح نموذج Product (models.py)

```python
from django.db import models  # استيراد وحدة models من Django لإنشاء النماذج

# تعريف فئة Product التي ترث من models.Model
class Product(models.Model):
    # حقل name: CharField لتخزين اسم المنتج كنص قصير
    # max_length=100: الحد الأقصى للطول هو 100 حرف
    name = models.CharField(max_length=100)
    
    # حقل description: TextField لتخزين وصف المنتج كنص طويل
    # لا يوجد حد أقصى للطول
    description = models.TextField()
    
    # حقل price: DecimalField لتخزين السعر كرقم عشري
    # max_digits=10: الحد الأقصى للأرقام هو 10
    # decimal_places=2: عدد المنازل العشرية هو 2
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # حقل created_at: DateTimeField لتخزين تاريخ ووقت الإنشاء
    # auto_now_add=True: يتم تعيين القيمة تلقائيًا عند إنشاء السجل
    created_at = models.DateTimeField(auto_now_add=True)

    # دالة __str__: تعيد تمثيل نصي للكائن
    # تستخدم في واجهة الإدارة وغيرها لعرض اسم المنتج
    def __str__(self):
        return self.name
```

## شرح مفصل:
- **from django.db import models**: هذا السطر يستورد الوحدة models من Django، والتي تحتوي على الفئات الأساسية لبناء النماذج.
- **class Product(models.Model)**: تعريف فئة Product التي ترث من models.Model، مما يجعلها نموذج Django.
- **name = models.CharField(max_length=100)**: حقل نصي قصير لاسم المنتج، محدود بـ100 حرف.
- **description = models.TextField()**: حقل نصي طويل لوصف المنتج، بدون حد.
- **price = models.DecimalField(max_digits=10, decimal_places=2)**: حقل رقمي عشري للسعر، بدقة 2 منازل عشرية.
- **created_at = models.DateTimeField(auto_now_add=True)**: حقل تاريخ ووقت، يتم تعيينه تلقائيًا عند الإنشاء.
- **def __str__(self)**: دالة خاصة تعيد تمثيل نصي للكائن، هنا اسم المنتج.