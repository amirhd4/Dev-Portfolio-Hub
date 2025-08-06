from django.shortcuts import render, get_object_or_404
from .models import Project

def project_list(request):
    # خواندن تمام پروژه‌ها از پایگاه داده و مرتب‌سازی بر اساس آخرین موارد اضافه شده
    projects = Project.objects.all().order_by('-id')

    # ارسال لیست پروژه‌ها به قالب
    context = {
        'projects': projects
    }
    return render(request, 'portfolio/project_list.html', context)


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    context = {
        'project': project
    }
    return render(request, 'portfolio/project_detail.html', context)