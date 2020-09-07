from django.contrib import admin

from .api.model.model import Bucket
from .api.model.model import Todo

# Register your models here.

admin.site.register(Bucket)
admin.site.register(Todo)