from rest_framework import generics
from .models import ToDo
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .serializers import ToDoSerializer

class ToDoListCreateAPIView(generics.ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class ToDoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


# THESE TWO FUNCTIONS ARE HANDLED BY API VIEW ABOVE, maybe?

# @csrf_exempt
# def todo_list(request):
#    todos = ToDo.objects.all()
#     serializer = ToDoSerializer(todos, many=True)
#     return JsonResponse(serializer.data, safe=False)

# @csrf_exempt
# def todo_create(request):
#     serializer = ToDoSerializer(data=request.POST)
#     if serializer.is_valid():
#         serializer.save()
#         return JsonResponse(serializer.data, status=201)
#     return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def todo_detail(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    serializer = ToDoSerializer(todo)
    return JsonResponse(serializer.data)

@csrf_exempt
def todo_update(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    serializer = ToDoSerializer(todo, data=request.POST)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def todo_delete(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    todo.delete()
    return JsonResponse({'message': 'Todo deleted successfully!'}, status=204)