from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CustomUserSerializer
from base.models import CustomUser
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser


@api_view(['GET', 'POST'])
def apiPostGet(request):
    if request.method == "GET":
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def apiPutDelete(request, user_id):
    if request.method == "GET":
        user = CustomUser.objects.get(id=user_id)
        serializer = CustomUserSerializer(user, many=False)
        return Response(serializer.data)
    elif request.method == "PUT":
        user = CustomUser.objects.get(id=user_id)
        serializer = CustomUserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == "DELETE":
        user = CustomUser.objects.get(id=user_id)
        user.delete()
        return Response("Item Deleted Successfully")


    


