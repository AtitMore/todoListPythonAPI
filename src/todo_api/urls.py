from django.contrib import admin
from django.urls import path, include
from rest_framework import routers 
from todos import views 
from todos.api.bucket_list import bucket_list
from todos.api.todo_list import todo_list

# router = routers.DefaultRouter()  
# router.register(r'todos', views.BucketView, 'todos')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include(router.urls))bucketList
    path('api/', views.apiOverview, name="api-overview"),
    path('bucket', bucket_list.bucketApiOverview, name="bucketApiOverview"),
    path('bucket/list/', bucket_list.bucketList, name="bucket-list"),
    path('bucket/add/', bucket_list.createBucket, name="bucket-add"),
	path('bucket/edit/<str:pk>/', bucket_list.bucketDetail, name="bucket-edit"),
    path('bucket/update/<str:pk>/', bucket_list.bucketUpdate, name="bucket-update"),
    path('bucket/delete/<str:pk>/', bucket_list.bucketDelete, name="bucket-delete"),

    path('todo', todo_list.todoApiOverview, name="todoApiOverview"),
    path('todo/list/', todo_list.todoList, name="todo-list"),
    path('todo/add/', todo_list.createTodo, name="todo-add"),
	path('todo/edit/<str:pk>/', todo_list.todoDetail, name="todo-edit"),
    path('todo/update/<str:pk>/', todo_list.todoUpdate, name="todo-update"),
    path('todo/delete/<str:pk>/', todo_list.todoDelete, name="todo-delete"),
]

