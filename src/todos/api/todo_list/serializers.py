from rest_framework import serializers
from todos.api.model.model import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'bucket_id')