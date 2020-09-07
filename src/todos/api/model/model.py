from django.db import models

class Bucket(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    completed = models.BooleanField(default=False, blank=True, null=True)

class Todo(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    completed = models.BooleanField(default=False, blank=True, null=True)
    bucket_id = models.ForeignKey(Bucket, on_delete=models.CASCADE)