from .models import student
from rest_framework import serializers

class stuserializer(serializers.ModelSerializer):
  class Meta:
    model=student
    fields='__all__'
    
