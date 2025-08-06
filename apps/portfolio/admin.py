from django.contrib import admin
from .models import Technology, Service, Project, Testimonial

# برای نمایش گواهی‌نامه‌ها در صفحه پروژه
class TestimonialInline(admin.TabularInline):
    model = Testimonial
    extra = 1 # تعداد فرم خالی برای اضافه کردن آیتم جدید

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'live_demo_url', "slug") # فیلدهایی که در لیست نمایش داده می‌شوند
    list_filter = ('technologies', 'services', "slug") # فیلدهایی برای فیلتر کردن در سایدبار
    search_fields = ('title', 'description') # فیلدهایی که قابل جستجو هستند
    inlines = [TestimonialInline] # اضافه کردن ویرایش گواهی‌نامه‌ها در همین صفحه

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    search_fields = ('name',)

# مدل‌های دیگر را به صورت ساده ثبت می‌کنیم
admin.site.register(Service)
admin.site.register(Testimonial)