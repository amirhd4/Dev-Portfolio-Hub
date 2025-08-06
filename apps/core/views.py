from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def home(request):
    return render(request, 'home.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # اگر فرم معتبر بود، داده‌ها را استخراج کن
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # ساخت متن ایمیل
            full_message = f"پیام جدید از طرف: {name} ({from_email})\n\n{message}"

            # ارسال ایمیل
            send_mail(
                subject=f'[فرم تماس سایت] {subject}',
                message=full_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['your_admin_email@example.com'],
            )

            return redirect('core:contact-success')
    else:
        form = ContactForm()

    context = {
        'form': form
    }
    return render(request, 'core/contact.html', context)

def contact_success_view(request):
    return render(request, 'core/contact_success.html')