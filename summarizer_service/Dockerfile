# summarizer_service/Dockerfile

FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# کپی کردن فایل نیازمندی‌ها
COPY requirements.txt .

# --- استراتژی نهایی ---

# مرحله ۱: pip را به آخرین نسخه ارتقا می‌دهیم (موفقیت‌آمیز بود)
RUN pip install --no-cache-dir --upgrade pip

# مرحله ۲: نسخه سبک torch (فقط CPU) را جداگانه نصب می‌کنیم (موفقیت‌آمیز بود)
RUN pip install --no-cache-dir --timeout 600 \
    torch --index-url https://download.pytorch.org/whl/cpu

# مرحله ۳: بقیه پکیج‌ها را از سرور اصلی PyPI نصب می‌کنیم.
# دیگر نیازی به میرور نیست چون پکیج‌های باقی‌مانده سبک هستند.
RUN pip install --no-cache-dir --timeout 600 -r requirements.txt

# کپی کردن بقیه کدهای سرویس
COPY . .

# مشخص کردن پورت سرویس
EXPOSE 8001

# اجرای سرویس با Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]