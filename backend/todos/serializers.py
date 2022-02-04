#todos/serializers
from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Todo
		fields = ('id','title','body',)	

# This serializer class will translate the model data to JSON format