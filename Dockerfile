# ---------------------------------------------------------------------
# STAGE 1: Frontend Builder - ساخت فایل‌های استاتیک
# ---------------------------------------------------------------------
# ما از یک ایمیج رسمی Node.js به عنوان "خط مونتاژ اول" استفاده می‌کنیم
FROM node:20-alpine AS frontend-builder

WORKDIR /app

# ابتدا فقط package.json را کپی می‌کنیم تا از کش داکر بهتر استفاده شود
COPY package*.json ./
# نصب تمام وابستگی‌های نود
RUN npm install

# کپی کردن بقیه فایل‌های پروژه برای دسترسی به tailwind.config.js و input.css
COPY . .
# ساخت فایل‌های CSS نهایی
RUN npm run build:css

# ---------------------------------------------------------------------
# STAGE 2: Final Python Application - ساخت ایمیج نهایی و سبک
# ---------------------------------------------------------------------
# حالا از ایمیج پایتون به عنوان "خط مونتاژ دوم" شروع می‌کنیم
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# نصب نیازمندی‌های بک‌اند
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# کپی کردن کدهای پایتون از پروژه محلی
COPY . .

# --- جادوی اصلی اینجاست ---
# کپی کردن فایل‌های ساخته شده از "خط مونتاژ اول" به "خط مونتاژ دوم"
COPY --from=frontend-builder /app/static/dist ./static/dist
COPY --from=frontend-builder /app/static/fonts ./static/fonts

# اجرای collectstatic با پرچم --clear برای جمع‌آوری فایل‌های تمیز
RUN python manage.py collectstatic --noinput --clear

# اجرای نهایی سرور Gunicorn
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "Dev_Portfolio_Hub.wsgi"]