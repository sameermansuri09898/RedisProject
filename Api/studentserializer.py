from .models import student,Data
from rest_framework import serializers

class stuserializer(serializers.ModelSerializer):
  class Meta:
    model=student
    fields='__all__'
    
class dataserializer(serializers.ModelSerializer):
  class Meta:
    model=Data
    fields='__all__'
    
