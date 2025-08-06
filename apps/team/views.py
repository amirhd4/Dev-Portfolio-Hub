from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
import json
from .models import TeamMember
from apps.portfolio.models import Technology

def team_list(request):
    # بهینه‌سازی کوئری با prefetch_related برای جلوگیری از خواندن چندباره از دیتابیس
    team_members = TeamMember.objects.prefetch_related('skills').all()

    # استخراج تمام تکنولوژی‌هایی که حداقل یک عضو تیم آن را دارد
    skills = Technology.objects.filter(teammember__isnull=False).distinct()

    # آماده‌سازی داده‌ها برای تبدیل به JSON و استفاده در Alpine.js
    team_members_for_js = []
    for member in team_members:
        team_members_for_js.append({
            'id': member.id,
            'name': member.name,
            'title': member.title,
            'photo_url': member.photo.url if member.photo else None,
            'bio': member.bio,
            'linkedin_url': member.linkedin_url,
            'github_url': member.github_url,
            'skills': [skill.name for skill in member.skills.all()]
        })

    context = {
        'team_members': team_members, # برای استفاده در صورت نیاز به رندر سمت سرور
        'skills': skills,
        # تبدیل لیست پایتونی به رشته JSON برای تزریق به جاوا اسکریپت
        'team_members_json': team_members_for_js
    }
    print(json.dumps(team_members_for_js, cls=DjangoJSONEncoder))
    return render(request, 'team/team_list.html', context)