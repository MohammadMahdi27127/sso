from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import SMS
from .Serializer import SMSSerializer
import requests  # برای ارسال پیامک با کاوه نگار
from kavenegar import *

@api_view(['GET'])
def create_sms(request):
    mobile = request.query_params.get('mobile')
    source = request.query_params.get('source')

    if mobile and source:
        sms_instance = SMS(mobile=mobile, source=source)
        sms_instance.save()


        send_sms(sms_instance.mobile, sms_instance.message)

        serializer = SMSSerializer(sms_instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response({"error": "وارد کردن شماره تلفن الزامی است"}, status=status.HTTP_400_BAD_REQUEST)

def send_sms(mobile, message):
    # اینجا باید کد مربوط به API کاوه نگار را قرار دهید
    # به عنوان مثال:
    url = "https://api.kavenegar.com/v1/YOUR_API_KEY/sms/send.json"
    data = {
        'receptor': mobile,
        'message': f'پیام شما: {message}'
    }
    response = requests.post(url, data=data)
    return response.json()
    api = KavenegarAPI('474D71646F756D4E6961784A4374742F4B4A63385142547546577246633179327A6254476576432B6A74553D')
    params = { 'sender' : '2000660110', 'receptor': '09109063654', 'message' :'.وب سرویس پیام کوتاه کاوه نگار' }
    response = api.sms_send(params)

    api = KavenegarAPI('Your API Key')
    params = {
        'sender': '1000xxxx',
        'receptor' : '0919xxxxxx',
        'message' : "Hello Python!"
    }
    response = api.sms_send(params)

@api_view(['POST'])
def verify_message(request):
    mobile = request.data.get('mobile')
    message = request.data.get('message')
    source = request.data.get('source')

    try:
        sms_instance = SMS.objects.get(mobile=mobile)

        if sms_instance.message == message:

            return Response({"message": "مقدار وارد شده صحیح می باشد،شما می توانید وارد سایت شوید"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "مقدار وارد شده معتبر نمی باشد"}, status=status.HTTP_400_BAD_REQUEST)

    except SMS.DoesNotExist:
        return Response({"error": "شماره شما پیدا نشد"}, status=status.HTTP_404_NOT_FOUND)