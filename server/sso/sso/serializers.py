from rest_framework import serializers
from .models import SMS

class SMSSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMS
        fields = ['id', 'mobile', 'token']