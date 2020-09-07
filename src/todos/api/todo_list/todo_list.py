from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets    
from todos.api.model.model import Todo
from .serializers import TodoSerializer

@api_view(['GET'])
def todoApiOverview(request):
	api_urls = {
		'List':'/todo-list/',
		'Detail View':'/todo-detail/<str:pk>/',
		'Create':'/todo-create/',
		'Update':'/todo-update/<str:pk>/',
		'Delete':'/todo-delete/<str:pk>/'
	}
	return Response(api_urls)


@api_view(['GET'])
def todoList(request):
	bucket = Todo.objects.all().order_by('-id')
	serializer = TodoSerializer(bucket, many=True)
	return Response(serializer.data)


@api_view(['POST'])
def createTodo(request):
	print("sdaskldjsa", request.data)
	serializer = TodoSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['GET'])
def todoDetail(request, pk):
	todo = Todo.objects.get(id=pk)
	serializer = TodoSerializer(todo, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def todoUpdate(request, pk):
	todo = Todo.objects.get(id=pk)
	serializer = TodoSerializer(instance=todo, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def todoDelete(request, pk):
	todo = Todo.objects.get(id=pk)
	todo.delete()

	return Response('Item succsesfully delete!')