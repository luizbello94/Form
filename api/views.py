from rest_framework import status 
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_api(request):
    return Response({"System":"online"})


@api_view(['POST'])
def post_message(request):
    return Response({"System":"Send message"})