from fastapi import FastAPI
from pydantic import BaseModel, Field
from transformers import pipeline
import torch

# ساخت اپلیکیشن FastAPI
app = FastAPI(title="Text Summarization Service")

# بارگذاری مدل هوش مصنوعی (ممکن است در اولین اجرا کمی طول بکشد تا مدل دانلود شود)
# ما از یک مدل بهینه و شناخته‌شده استفاده می‌کنیم
try:
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
except Exception as e:
    print(f"Error loading model: {e}")
    summarizer = None

# تعریف مدل ورودی و خروجی با Pydantic برای اعتبارسنجی خودکار
class TextInput(BaseModel):
    text: str = Field(..., min_length=100, title="Text to summarize", description="Must be at least 100 characters long.")

class SummaryOutput(BaseModel):
    summary: str

@app.post("/summarize/", response_model=SummaryOutput, summary="Summarize a piece of text")
def summarize_text(payload: TextInput):
    """
    Receives a long text and returns its summary.
    """
    if summarizer is None:
        return {"summary": "Model is not available."}

    result = summarizer(payload.text, max_length=150, min_length=30, do_sample=False)
    return {"summary": result[0]['summary_text']}

@app.get("/")
def read_root():
    return {"status": "Summarization service is running."}