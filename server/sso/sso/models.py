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


class auth_user(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    password=models.CharField(max_length=128,null=False,blank=False)
    last_login = models.DateTimeField(auto_now=True)
    is_superuser = models.BooleanField(default=False)
    username = models.CharField(max_length=150,null=False,blank=False,unique=True)
    last_name = models.CharField(max_length=150,null=False,blank=False)
    email = models.CharField(max_length=254,null=False,blank=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=150,null=False,blank=False)