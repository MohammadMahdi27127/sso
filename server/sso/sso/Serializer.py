from rest_framework import serializers
from .models import SMS

class SMSSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMS
        fields = ['mobile', 'message', 'source', 'date']  # فیلدهای مدل SMS
        read_only_fields = ['message', 'date']  # توکن و تاریخ فقط برای خواندن