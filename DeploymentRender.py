1️⃣ تجهيز المشروع

DEBUG = False في settings.py

ALLOWED_HOSTS = ['*'] (أو اسم الدومين النهائي)

إعداد static files:

python manage.py collectstatic


إنشاء requirements.txt:

pip freeze > requirements.txt


إنشاء Procfile (مهم لـ Render):

web: gunicorn yourprojectname.wsgi


استخدم قاعدة بيانات مناسبة (PostgreSQL يفضل على الإنتاج، أو SQLite لمشاريع صغيرة).

2️⃣ رفع المشروع على GitHub

ارفع كل الكود على repo جديد.

3️⃣ إنشاء مشروع على Render

سجل دخولك على Render

اختر New Web Service → Connect a GitHub repo

حدد repo مشروعك

Runtime: Python 3.x

Build Command:

pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput


Start Command:

gunicorn yourprojectname.wsgi


أضف أي Environment Variables:

SECRET_KEY

DEBUG=False

Database URL أو أي إعدادات مهمة

4️⃣ تجربة المشروع

بعد ما Render يخلص build & deploy، هيديك رابط مباشر للمشروع.

افتح /swagger/ أو /api/docs/ على الرابط ده، هتلاقي API Documentation شغالة على الإنترنت.

🔹 النتيجة النهائية

كل الـ endpoints مرئية وجاهزة للمستخدمين والمطورين

مشروعك شغال على الإنترنت، ممكن تعمل POST/GET وتشوف النتائج مباشرة

جاهز للاختبارات أو مشاركة المشروع مع الآخرين