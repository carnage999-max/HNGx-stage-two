from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PersonSerializer
from base.models import Person
from django.http import HttpResponse


@api_view(['GET', 'POST'])
def apiPostGet(request):
    if request.method == "GET":
        users = Person.objects.all()
        serializer = PersonSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def apiPutDelete(request, user_id):
    if request.method == "GET":
        print(Person.objects.get(id=user_id))
        try:
            user = Person.objects.get(id=user_id)
            print(user)
            serializer = PersonSerializer(user, many=False)
            return Response(serializer.data)
        except:
            return HttpResponse(f"A user with id {user_id} does not exist")
    elif request.method == "PUT":
        user = Person.objects.get(id=user_id)
        serializer = PersonSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == "DELETE":
        user = Person.objects.get(id=user_id)
        user.delete()
        return Response("Item Deleted Successfully")


    


