from rest_framework.decorators import api_view
from .serializers import PersonSerializer
from base.models import Person
from django.http import JsonResponse


@api_view(['GET', 'POST'])
def apiPostGet(request):
    if request.method == "GET":
        users = Person.objects.all()
        serializer = PersonSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False, status=200)
        else:
            return JsonResponse({"errors": serializer.errors}, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def apiPutDelete(request, user_id):
    if request.method == "GET":
        try:
            user = Person.objects.get(id=user_id)
            serializer = PersonSerializer(user, many=False)
            return JsonResponse(serializer.data, safe=False)
        except:
            return JsonResponse({"error": f"A user with ID {user_id} does not exist"}, status=400)
    elif request.method == "PUT":
        user = Person.objects.get(id=user_id)
        serializer = PersonSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
    elif request.method == "DELETE":
        try:
            user = Person.objects.get(id=user_id)
            user.delete()
            return JsonResponse({"response": "Person Deleted Successfully"}, safe=False, status=204)
        except:
            return JsonResponse({"error": "Person does not exist"}, safe=False, status=400)
