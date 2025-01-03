from django.db import models
import random
import string
from django.utils import timezone

class SMS(models.Model):
    id=models.AutoField(primary_key=True,null=False)
    mobile = models.IntegerField(max_length=15,null=False)  # شماره موبایل
    message = models.CharField(max_length=5,unique=True,null=False)  # توکن 5 حرفی
    source = models.CharField(max_length=50)  # مبدا
    date = models.DateTimeField(auto_now_add=True)  # تاریخ و زمان ایجاد

    def save(self, *args, **kwargs):
        # تولید توکن 5 حرفی یکتا
        self.message = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        super().save(*args, **kwargs)

class Token(models.Model):
    id=models.AutoField(primary_key=True,null=False)
    token = models.CharField(max_length=5,null=False)
    soruse=models.ForeignKey(SMS,null=False,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    mobile = models.ForeignKey(SMS,null=False,on_delete=models.CASCADE)


class User(models.Model):
    id=models.AutoField(primary_key=True,null=False)
    soruse=models.ForeignKey(SMS,null=False)
    date = models.DateTimeField(auto_now_add=True)

