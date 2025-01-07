import requests  # برای ارسال پیامک با کاوه نگار
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import SMS
from .serializers import SMSSerializer

@api_view(['POST'])
def create_phone_number(request):
    serializer = SMSSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# def send_sms(mobile, token):
#     # اینجا باید کد مربوط به API کاوه نگار را قرار دهید
#     # به عنوان مثال:
#     url = "https://api.kavenegar.com/v1/YOUR_API_KEY/sms/send.json"
#     data = {
#         'receptor': mobile,
#         'message': f'Your token is: {token}'
#     }
#     response = requests.post(url, data=data)
#     return response.json()
#
# @api_view(['POST'])
# def verify_token(request):
#     mobile = request.data.get('mobile')
#     token = request.data.get('token')
#     source = request.data.get('source')
#
#     try:
#         sms_instance = SMS.objects.get(mobile=mobile)
#
#         if sms_instance.token == token:
#             # اگر توکن معتبر بود، کاربر می‌تواند به سایت پذیرنده هدایت شود
#             return Response({"message": "Token is valid. You can access the site."}, status=status.HTTP_200_OK)
#         else:
#             return Response({"error": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST)
#
#     except SMS.DoesNotExist:
#         return Response({"error": "Phone number not found."}, status=status.HTTP_404_NOT_FOUND)