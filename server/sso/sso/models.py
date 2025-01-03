from django.db import models
import random
import string

class SMS(models.Model):
    id = models.AutoField(primary_key=True)
    mobile = models.CharField(max_length=11, unique=True)
    message = models.TextField(max_length=5,unique=True,null=False,blank=False)
    source = models.CharField(max_length=50,null=False,blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.message = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        super().save(*args, **kwargs)

class token(models.Model):
    id = models.AutoField(primary_key=True)
    token = models.CharField(max_length=5,unique=True,null=False,blank=False)
    date = models.DateTimeField(auto_now_add=True)
    source=models.ForeignKey(SMS,on_delete=models.CASCADE,related_name='tokens')
    phone=models.ForeignKey(SMS,on_delete=models.CASCADE,related_name='phones')


class User(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    source=models.ForeignKey(SMS,on_delete=models.CASCADE,related_name='users')
