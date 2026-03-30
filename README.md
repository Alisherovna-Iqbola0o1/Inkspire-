📚 Inspire


Inspire 📚 – Django va Django REST Framework yordamida yaratilgan, ishlab chiqarishga tayyor motivatsion va ilhomlantiruvchi kontent platformasi backend tizimi. Loyihada foydalanuvchilar, postlar, sharhlar (reviews), tavsiyalar (recommendations) va ro‘llar asosida autentifikatsiya (mijoz, admin) mavjud.

Foydalanuvchilar ilhomlantiruvchi postlarni yaratish, ko‘rish va baholashlari mumkin. Adminlar esa platformani boshqarish, kontentni monitoring qilish va foydalanuvchilarni nazorat qilish imkoniyatiga ega. Tizim media fayllarni yuklash, CORS orqali frontend bilan integratsiya, va JWT autentifikatsiya orqali xavfsiz API kirishini qo‘llab-quvvatlaydi.


---🚀 Asosiy funksiyalar
Foydalanuvchilarni boshqarish: ro‘yxatdan o‘tish, login, profilni yangilash
Postlar: motivatsion va ilhomlantiruvchi kontentni yaratish, tahrirlash, o‘chirish va ko‘rish
Sharhlar (Reviews): foydalanuvchilar postlarga sharh qoldirishi va reyting berishi mumkin
Tavsiyalar (Recommendations): foydalanuvchilar uchun tavsiya tizimi
Rol asosida autentifikatsiya: mijoz, admin
Media fayllar: post rasmlari va media fayllarni yuklash imkoniyati
CORS qo‘llab-quvvatlash: frontend bilan muammosiz integratsiya
Qidiruv: ilhomlantiruvchi postlarni tezkor qidirish (optional, ElasticSearch orqali)


---🛠️ Texnologiyalar
Backend: Django, Django REST Framework
Autentifikatsiya: JWT (JSON Web Token)
Database: SQLite (default) / PostgreSQL orqali sozlanadi
CORS: django-cors-headers
Muhit sozlamalari: python-dotenv
Email backend: konsol (development uchun)
Qidiruv: ElasticSearch (optional)


---⚙️ O‘rnatish va ishga tushirish
Repository-ni klon qilish
git clone <repository_url>
cd Inspire
Virtual environment yaratish va faollashtirish
python -m venv venv
source venv/bin/activate
# Windows: venv\Scripts\activate
Talab qilinadigan paketlarni o‘rnatish
pip install -r requirements.txt
Muhit sozlamalari (.env fayli)

.env faylini yaratib, quyidagilarni qo‘shing:

SECRET_KEY=your_secret_key
DEBUG=True
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
ELASTICSEARCH_HOST=localhost:9200
Migratsiyalarni bajarish
python manage.py migrate
Admin user yaratish (optional)
python manage.py createsuperuser
Serverni ishga tushirish
python manage.py runserver


---📌 API manzillari

Endpoint	Funksiya	Rol
/api/users/register/	Foydalanuvchi ro‘yxatdan o‘tishi	Barcha
/api/users/login/	JWT login	Barcha
/api/users/profile/	Profilni ko‘rish/yangilash	Authenticated
/api/users/users/	Foydalanuvchilar ro‘yxati	Admin
/api/posts/	Postlarni CRUD	Authenticated
/api/reviews/	Postlar uchun sharhlar	Authenticated
/api/recommendations/	Tavsiyalarni ko‘rish	Authenticated
/admin/	Admin panel	Admin


---🤝 Hissa qo‘shish

Hissalar qabul qilinadi!

git checkout -b feature-name
git commit -m "Add feature"
git push origin feature-name