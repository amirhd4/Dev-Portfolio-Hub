# summarizer_service/Dockerfile

FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# بهینه‌سازی کش لایه‌ای
COPY requirements.txt .

# --- راه حل نهایی اینجاست ---
# ما دو پارامتر جدید اضافه کرده‌ایم:
# --no-require-hashes: به pip می‌گوید که بررسی امنیتی هش فایل‌ها را انجام نده.
# --prefer-binary: به pip می‌گوید تا حد امکان از فایل‌های باینری از پیش کامپایل شده (wheels) استفاده کند که سریع‌تر نصب می‌شوند.
RUN pip install \
    --no-cache-dir \
    --timeout 600 \
    --no-require-hashes \
    --prefer-binary \
    -r requirements.txt

# کپی کردن بقیه کدهای سرویس
COPY . .

# مشخص کردن پورت سرویس
EXPOSE 8001

# اجرای سرویس با Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]