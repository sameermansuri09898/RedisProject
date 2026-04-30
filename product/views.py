from django.shortcuts import render
from Api.models import student
from rest_framework import generics
from Api.studentserializer import stuserializer
from rest_framework.filters import SearchFilter
class result(generics.ListAPIView):
  queryset=student.objects.all()
  serializer_class=  stuserializer
  filter_backends=[SearchFilter]
  search_fields = ['name']
