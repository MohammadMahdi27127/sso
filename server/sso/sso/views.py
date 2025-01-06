from kavenegar.KavenegarAPI import sms_send
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from .models import SMS
from .serializers import SMSSerializer
from django.core.exceptions import ValidationError

class SendTokenView(generics.CreateAPIView):
    queryset = SMS.objects.all()
    serializer_class = SMSSerializer



    def create(self, request, *args, **kwargs):
        mobile = request.data.get('mobile')
        source = request.data.get('source')

        if not mobile or len(mobile) != 11:
            return Response({"error": "شماره موبایل نامعتبر است."}, status=status.HTTP_400_BAD_REQUEST)

        sms = SMS(mobile=mobile, source=source)
        sms.save()
        sms_send(mobile, sms.token)

        return Response({"message": "پیامک ارسال شد.", "token": sms.token}, status=status.HTTP_201_CREATED)


# def redirect_to_source(source, token):
#     pass
#
#
# class VerifyTokenView(generics.GenericAPIView):
#     def post(self, request, *args, **kwargs):
#         mobile = request.data.get('mobile')
#         token = request.data.get('token')
#
#         try:
#             sms = SMS.objects.get(mobile=mobile, token=token)
#             # ورود به سایت پذیرنده و ارسال توکن
#             redirect_to_source(sms.source, token)
#             return Response({"message": "ورود موفقیت‌آمیز بود."}, status=status.HTTP_200_OK)
#         except SMS.DoesNotExist:
#             return Response({"error": "توکن یا شماره موبایل نامعتبر است."}, status=status.HTTP_400_BAD_REQUEST)