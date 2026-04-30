from django.shortcuts import render
from Api.models import student,Data
from rest_framework import generics
from Api.studentserializer import dataserializer
from rest_framework.filters import SearchFilter
class result(generics.ListAPIView):
  queryset=Data.objects.all()
  serializer_class=  dataserializer
  filter_backends=[SearchFilter]
  search_fields = ['client_name']
