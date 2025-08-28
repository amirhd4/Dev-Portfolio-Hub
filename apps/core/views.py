from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from apps.portfolio.models import Project, Service, Technology, Testimonial
from apps.team.models import TeamMember


from django.shortcuts import render
from apps.portfolio.models import Project, Testimonial

def home(request):
    featured_projects = Project.objects.all()[:6]
    services = Service.objects.all()
    technologies = Technology.objects.all()[:12]
    testimonials = Testimonial.objects.select_related('project').all()[:3]
    team_members = TeamMember.objects.prefetch_related('skills').all()[:6]

    context = {
        'featured_projects': featured_projects,
        'services': services,
        'technologies': technologies,
        'testimonials': testimonials,
        'team_members': team_members,
    }
    return render(request, 'home.html', context)

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