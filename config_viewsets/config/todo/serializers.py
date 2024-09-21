from rest_framework import serializers
from . import models



class Todoserializer(serializers.ModelSerializer):
    class Meta:
        model=models.Todo
        fields='__all__'