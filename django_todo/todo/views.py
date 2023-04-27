from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ToDo
from .serializers import ToDoSerializer


class ToDoListCreateAPIView(generics.ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class ToDoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


@api_view(['GET'])
def todo_list(request):
    todos = ToDo.objects.all()
    serializer = ToDoSerializer(todos, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def todo_create(request):
    serializer = ToDoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def todo_detail(request, pk):
    try:
        todo = ToDo.objects.get(pk=pk)
    except ToDo.DoesNotExist:
        return Response(status=404)

    serializer = ToDoSerializer(todo)
    return Response(serializer.data)


@api_view(['PUT'])
def todo_update(request, pk):
    try:
        todo = ToDo.objects.get(pk=pk)
    except ToDo.DoesNotExist:
        return Response(status=404)

    serializer = ToDoSerializer(todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def todo_delete(request, pk):
    try:
        todo = ToDo.objects.get(pk=pk)
    except ToDo.DoesNotExist:
        return Response(status=404)

    todo.delete()
    return Response(status=204)
