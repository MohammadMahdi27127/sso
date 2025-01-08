from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SMSSerializer


@api_view(['POST'])
def create_mobile(request):
    serializer = SMSSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        mobile = serializer.validated_data['mobile']
        # sms_send(mobile)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



