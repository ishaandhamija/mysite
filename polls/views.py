from django.core.serializers import serialize
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from polls.models import A


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


@api_view(http_method_names=['GET'])
def get_ass(request):

    ass = A.objects.all()

    return Response(
        data=serialize('json', ass),
        status=status.HTTP_200_OK
    )
