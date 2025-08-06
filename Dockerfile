# Dockerfile (ریشه اصلی پروژه) - نسخه نهایی و پروداکشن

FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# تمام کدهای پروژه را کپی کن
COPY . .

# --- تغییرات کلیدی اینجاست ---
# ۱. اجرای collectstatic برای جمع‌آوری تمام فایل‌های استاتیک در پوشه /app/staticfiles/
# Nginx از این پوشه برای سرویس‌دهی فایل‌ها استفاده خواهد کرد.
RUN python manage.py collectstatic --noinput

# ۲. تغییر دستور اجرا از runserver به Gunicorn
# Gunicorn یک سرور WSGI حرفه‌ای است که پشت Nginx قرار می‌گیرد.
# نکته: نام "portfolio_project" را با نام پوشه تنظیمات پروژه خود جایگزین کنید اگر متفاوت است.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "portfolio_project.wsgi"]