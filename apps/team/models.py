from django.db import models
from apps.portfolio.models import Technology # وارد کردن مدل تکنولوژی از اپ دیگر

# مدل اعضای تیم
class TeamMember(models.Model):
    name = models.CharField("نام کامل", max_length=100)
    title = models.CharField("عنوان شغلی", max_length=100)
    bio = models.TextField("بیوگرافی")
    photo = models.ImageField("عکس", upload_to='team_photos/')
    email = models.EmailField("ایمیل")
    linkedin_url = models.URLField("لینک لینکدین", blank=True, null=True)
    github_url = models.URLField("لینک گیت‌هاب", blank=True, null=True)
    skills = models.ManyToManyField(Technology, verbose_name="مهارت‌ها", blank=True)

    class Meta:
        verbose_name = "عضو تیم"
        verbose_name_plural = "اعضای تیم"

    def __str__(self):
        return self.name