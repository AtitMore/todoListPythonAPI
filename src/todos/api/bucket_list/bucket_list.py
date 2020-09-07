from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets    
from todos.api.model.model import Bucket
from .serializers import BucketSerializer

@api_view(['GET'])
def bucketApiOverview(request):
	api_urls = {
		'List':'/bucket-list/',
		'Detail View':'/bucket-detail/<str:pk>/',
		'Create':'/bucket-create/',
		'Update':'/bucket-update/<str:pk>/',
		'Delete':'/bucket-delete/<str:pk>/'
	}
	return Response(api_urls)


@api_view(['GET'])
def bucketList(request):
	bucket = Bucket.objects.all().order_by('-id')
	serializer = BucketSerializer(bucket, many=True)
	return Response(serializer.data)


@api_view(['POST'])
def createBucket(request):
	print("sdaskldjsa", request.data)
	serializer = BucketSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['GET'])
def bucketDetail(request, pk):
	todo = Bucket.objects.get(id=pk)
	serializer = BucketSerializer(todo, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def bucketUpdate(request, pk):
	todo = Bucket.objects.get(id=pk)
	serializer = BucketSerializer(instance=todo, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def bucketDelete(request, pk):
	todo = Bucket.objects.get(id=pk)
	todo.delete()

	return Response('Item succsesfully delete!')

