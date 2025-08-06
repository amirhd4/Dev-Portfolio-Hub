# summarizer_service/Dockerfile

FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# کپی کردن فایل نیازمندی‌ها
COPY requirements.txt .

# --- راه حل نهایی و سه مرحله‌ای ---

# مرحله ۱: pip را به آخرین نسخه ارتقا می‌دهیم
RUN pip install --no-cache-dir --upgrade pip

# مرحله ۲: نسخه بسیار سبک‌تر torch (فقط برای CPU) را از سرور مخصوص خودش نصب می‌کنیم.
# این کار حجم دانلود را از چند گیگابایت به حدود ۲۰۰ مگابایت کاهش می‌دهد.
RUN pip install --no-cache-dir --timeout 600 \
    torch --index-url https://download.pytorch.org/whl/cpu

# مرحله ۳: بقیه پکیج‌ها را از یک سرور آینه‌ای معتبر در آلمان نصب می‌کنیم.
# این کار سرعت و پایداری دانلود را به شدت افزایش می‌دهد.
RUN pip install --no-cache-dir --timeout 600 \
    --index-url https://ftp.fau.de/pypi/simple/ \
    -r requirements.txt

# کپی کردن بقیه کدهای سرویس
COPY . .

# مشخص کردن پورت سرویس
EXPOSE 8001

# اجرای سرویس با Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]