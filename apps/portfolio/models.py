from django.db import models
from slugify import slugify


# مدل تکنولوژی‌ها
class Technology(models.Model):
    name = models.CharField("نام تکنولوژی", max_length=100)
    icon = models.FileField("آیکون", upload_to='technologies/', null=True, blank=True)

    class Meta:
        verbose_name = "تکنولوژی"
        verbose_name_plural = "تکنولوژی‌ها"

    def __str__(self):
        return self.name


# مدل خدمات
class Service(models.Model):
    name = models.CharField("نام سرویس", max_length=100)
    description = models.TextField("توضیحات")
    icon = models.FileField("آیکون", upload_to='services/', null=True, blank=True)

    class Meta:
        verbose_name = "سرویس"
        verbose_name_plural = "سرویس‌ها"

    def __str__(self):
        return self.name



class Project(models.Model):
    title = models.CharField("عنوان پروژه", max_length=200)
    # این فیلد جدید را اضافه کنید
    slug = models.SlugField("اسلاگ (آدرس URL)", max_length=220, unique=True, blank=True, allow_unicode=True)
    description = models.TextField("توضیحات کوتاه")
    image = models.ImageField("تصویر اصلی", upload_to='projects/')
    case_study_content = models.TextField("محتوای مطالعه موردی (Markdown)")
    live_demo_url = models.URLField("لینک دموی زنده", blank=True, null=True)
    technologies = models.ManyToManyField(Technology, verbose_name="تکنولوژی‌های استفاده شده")
    services = models.ManyToManyField(Service, verbose_name="سرویس‌های ارائه شده")

    class Meta:
        verbose_name = "پروژه"
        verbose_name_plural = "پروژه‌ها"
        ordering = ['-id'] # مرتب‌سازی پیش‌فرض پروژه‌ها

    def __str__(self):
        return self.title

    # این متد را برای تولید خودکار اسلاگ اضافه کنید
    def save(self, *args, **kwargs):
        if not self.slug:
            # از عنوان پروژه یک اسلاگ فارسی و تمیز بساز
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)




# مدل گواهی‌نامه‌ها (نظرات مشتریان)
class Testimonial(models.Model):
    client_name = models.CharField("نام مشتری", max_length=100)
    client_title = models.CharField("عنوان شغلی مشتری", max_length=100)
    quote = models.TextField("نقل قول")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="testimonials",
                                verbose_name="پروژه مرتبط")

    class Meta:
        verbose_name = "گواهی‌نامه"
        verbose_name_plural = "گواهی‌نامه‌ها"

    def __str__(self):
        return f'نظر {self.client_name} درباره پروژه {self.project.title}'