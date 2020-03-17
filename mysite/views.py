from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response


@api_view(http_method_names=['GET'])
def ping(request):
    print ('log aaya')
    return Response(data='Pinged', status=status.HTTP_200_OK)
