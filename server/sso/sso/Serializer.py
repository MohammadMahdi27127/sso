from rest_framework import serializers
from .model import SMS, User, Token


class SMSSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMS
        fields = ['mobile', 'message', 'source', 'date']  # اضافه کردن فیلدهای جدید
        read_only_fields = ['message', 'date']  # توکن و تاریخ فقط برای خواندن

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        read_only_fields = ['date', 'soruse','token']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        read_only_fields = ['soruse','date']