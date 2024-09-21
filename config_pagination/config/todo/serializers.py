from rest_framework import serializers
from . import models
from django.contrib.auth import get_user_model



User = get_user_model()



class Todoserializer(serializers.ModelSerializer):
    class Meta:
        model=models.Todo
        fields='__all__'
        
        
        
class UserSerialzier(serializers.ModelSerializer):
    todos = Todoserializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = '__all__'        