from django.contrib import admin
from .models import TeamMember

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'email')
    search_fields = ('name', 'title', 'bio')
    list_filter = ('skills',)