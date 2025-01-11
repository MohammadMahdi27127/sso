
import random
import string
from django.db import models


class SMS(models.Model):
    id = models.AutoField(primary_key=True)
    mobile = models.CharField(max_length=15)  # تغییر به CharField
    source = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    token = models.CharField(max_length=5)

    def save(self, *args, **kwargs):
        # تولید یک توکن تصادفی
        while True:
            self.token = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
            if not SMS.objects.filter(token=self.token).exists():
                break
        super().save(*args, **kwargs)


class Token(models.Model):
    id = models.AutoField(primary_key=True)
    token = models.ForeignKey(SMS, on_delete=models.CASCADE, verbose_name='پیام', related_name='Tokens')
    date = models.DateTimeField(auto_now_add=True)
    mobile = models.ForeignKey(SMS, on_delete=models.CASCADE, verbose_name='موبایل', related_name='mobiles')
    source = models.ForeignKey(SMS, on_delete=models.CASCADE, related_name='sources')


class User(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    source = models.ForeignKey(SMS, on_delete=models.CASCADE, verbose_name='مبدا', related_name='users')