from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets             
from .api.model.model import Todo           

# class View(viewsets.ModelViewSet):       
#     serializer_class = TodoSerializer          
#     queryset = Bucket.objects.all()

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/todo-list/',
		'Detail View':'/todo-detail/<str:pk>/',
		'Create':'/todo-create/',
		'Update':'/todo-update/<str:pk>/',
		'Delete':'/todo-delete/<str:pk>/',
	}

	return Response(api_urls)

@api_view(['GET'])
def todoList(request):
	tasks = TodoList.objects.all().order_by('-id')
	serializer = TodoSerializer(tasks, many=True)
	return Response(serializer.data)



# @api_view(['GET'])
# def bucketList(request):
# 	tasks = TodoList.objects.all().order_by('-id')
# 	serializer = TodoSerializer(tasks, many=True)
# 	return Response(serializer.data)

# @api_view(['GET'])
# def todoDetail(request, pk):
# 	tasks = TodoList.objects.get(id=pk)
# 	serializer = TodoSerializer(tasks, many=False)
# 	return Response(serializer.data)
