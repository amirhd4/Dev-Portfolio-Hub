# summarizer_service/Dockerfile - نسخه نهایی با pre-loading مدل

FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir --timeout 600 \
    torch --index-url https://download.pytorch.org/whl/cpu
RUN pip install --no-cache-dir --timeout 600 -r requirements.txt

# تمام کدهای سرویس (شامل main.py و download_model.py) را کپی کن
COPY . .

# --- تغییر کلیدی اینجاست ---
# اسکریپت دانلود مدل را در زمان build اجرا می‌کنیم
# به لطف ولوم کش huggingface، این دانلود فقط یک بار انجام می‌شود.
RUN python download_model.py

EXPOSE 8001

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]