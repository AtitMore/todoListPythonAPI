from rest_framework import serializers
from .model.TodoList import TodoList

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ('id', 'title', 'description', 'completed')