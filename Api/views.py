from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .studentserializer import stuserializer
from .models import student
from django.core.cache import cache
from .rate_limiting import rate_limits

class studentview(APIView):
  @rate_limits(10,60)
  def post(self,request):
    serializer=stuserializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    serializer.save()
    return Response({
      "mssg":"student created successfully"
    })

class studentget(APIView):
    @rate_limits(5,60)
    def get(self, request):
        set_key = 'cached-student'

        cached_data = cache.get(set_key)
        if cached_data is not None:
            return Response(cached_data)

        studata = student.objects.all()
        serializer = stuserializer(studata, many=True)

        cache.set(set_key, serializer.data, timeout=300)

        return Response(serializer.data)