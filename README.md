# موقع الدعاية والإعلان

مشروع Django بسيط لعرض منتجات الدعاية والإعلان.

## المتطلبات
- Python 3.10
- Django 5.2.7

## التثبيت
1. استنسخ المستودع:
   ```bash
   git clone https://github.com/M0-h65/zooooook.git
   cd zooooook
   ```

2. قم بتثبيت المتطلبات:
   ```bash
   pip install django
   ```

3. قم بتشغيل الترحيلات:
   ```bash
   python manage.py migrate
   ```

4. أنشئ مستخدم إدارة:
   ```bash
   python manage.py createsuperuser
   ```

5. شغل الخادم:
   ```bash
   python manage.py runserver
   ```

## الاستخدام
- افتح `http://127.0.0.1:8000/products/` لرؤية قائمة المنتجات.
- اذهب إلى `http://127.0.0.1:8000/admin/` لإدارة المنتجات.

## الملفات المهمة
- `models_explanation.md`: شرح مفصل لنموذج Product.
- `views_explanation.md`: شرح مفصل لعرض product_list.
- `.github/copilot-instructions.md`: تعليمات للذكاء الاصطناعي.

## الميزات
- عرض قائمة المنتجات.
- واجهة إدارة Django لإضافة المنتجات.
- دعم اللغة العربية (RTL).