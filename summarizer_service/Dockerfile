# summarizer_service/Dockerfile

FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# بهینه‌سازی کش لایه‌ای: ابتدا فقط فایل نیازمندی‌ها را کپی می‌کنیم.
COPY requirements.txt .

# --- راه حل اصلی اینجاست ---
# افزایش زمان انتظار (timeout) برای pip به 600 ثانیه (10 دقیقه)
# این کار به شبکه شما زمان بسیار بیشتری برای دانلود فایل‌های حجیم می‌دهد.
RUN pip install --no-cache-dir --timeout 600 -r requirements.txt

# کپی کردن بقیه کدهای سرویس
COPY . .

# مشخص کردن پورت سرویس
EXPOSE 8001

# اجرای سرویس با Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]