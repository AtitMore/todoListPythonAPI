from rest_framework import serializers
from todos.api.model.model import Bucket

class BucketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bucket
        fields = ('id', 'title', 'description', 'completed')