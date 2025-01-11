from rest_framework import serializers
from .models import SMS


class SMSSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMS
        fields = ['mobile', 'source', 'message', 'token']  # اضافه کردن فیلدهای دیگر در صورت نیاز



class SMSDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = SMS
        fields = ['mobile', 'token', 'date']  # فیلدهایی که می‌خواهید نمایش دهید