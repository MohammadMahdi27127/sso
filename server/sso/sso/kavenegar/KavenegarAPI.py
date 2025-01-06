from kavenegar import *
from rest_framework.response import Response


def sms_send(self, response, ):
    api = KavenegarAPI('474D71646F756D4E6961784A4374742F4B4A63385142547546577246633179327A6254476576432B6A74553D')
    params = {'sender': '2000660110', 'receptor': '09109063654', 'message': '.وب سرویس پیام کوتاه کاوه نگار'}
    response = api.sms_send(params)
