from django.shortcuts import render
from . import models
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .import serializers
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework import viewsets
# Create your views here.



#region function base view

# دریافت  و پست کردن دیتا جدید و نمایش به صورتی لیست تمام دیتاها


@api_view(['GET','POST'])
def all_todos(request:Request):
    if request.method=='GET':   
        todos=models.Todo.objects.order_by('priority').all()
        todo_serializer=serializers.Todoserializer(todos,many=True)
        return Response(todo_serializer.data,status.HTTP_200_OK)
    elif request.method=='POST':
        
        serializer=serializers.Todoserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
            
    return Response(None,status.HTTP_400_BAD_REQUEST)        
        



# دریافت تک دیتا و حذف و یا ادیت آن
 
@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail_view(request: Request, todo_id:int):
    try:
        todo = models.Todo.objects.get(pk=todo_id)
    except models.Todo.DoesNotExist:
        return Response(None, status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = serializers.Todoserializer(todo)
        return Response(serializer.data, status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = serializers.Todoserializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        return Response(None, status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        todo.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)        
    
    
    
    
    # endregion

#region class base view


# همان ساختار به صورت classbaseview

class TodosListApiView(APIView):
    def get(self, request: Request):
        todos = models.Todo.objects.order_by('priority').all()
        todo_serializer = serializers.Todoserializer(todos, many=True)
        return Response(todo_serializer.data, status.HTTP_200_OK)

    def post(self, request: Request):
        serializer = serializers.Todoserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(None, status.HTTP_400_BAD_REQUEST)




class TodosDetailApiView(APIView):
    def get_object(self, todo_id: int):
        try:
            todo = models.Todo.objects.get(pk=todo_id)
            return todo
        except models.Todo.DoesNotExist:
            return Response(None, status.HTTP_404_NOT_FOUND)


    def get(self, request: Request, todo_id:int):
        todo = self.get_object(todo_id)
        serializer = serializers.Todoserializer(todo)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request: Request, todo_id:int):
        todo = self.get_object(todo_id)
        serializer = serializers.Todoserializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        return Response(None, status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, todo_id:int):
        todo = self.get_object(todo_id)
        todo.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)

#endregion

#region mixins

class TodosListMixinApiView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = models.Todo.objects.order_by('priority').all()
    serializer_class = serializers.TodoSerializer

    def get(self, request: Request):
        return self.list(request)
    
    def post(self, request: Request):
        return self.create(request)


class TodosDetailMixinApiView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = models.Todo.objects.order_by('priority').all()
    serializer_class = serializers.TodoSerializer

    def get(self, request: Request, pk):
        return self.retrieve(request, pk)

    def put(self, request: Request, pk):
        return self.update(request, pk)

    def delete(self, request: Request, pk):
        return self.destroy(request, pk)

#endregion



#region generics

class TodosGenericApiView(generics.ListCreateAPIView):
    queryset = models.Todo.objects.order_by('priority').all()
    serializer_class = serializers.TodoSerializer


class TodosGenericDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Todo.objects.order_by('priority').all()
    serializer_class = serializers.TodoSerializer

#endregion


#region viewsets

class TodosViewSetApiView(viewsets.ModelViewSet):
    queryset = models.Todo.objects.order_by('priority').all()
    serializer_class = serializers.TodoSerializer

#endregion