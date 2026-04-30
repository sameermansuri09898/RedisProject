from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .studentserializer import stuserializer,dataserializer
from .models import student,Data
from django.core.cache import cache
from .rate_limiting import rate_limits
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

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


class Fetchdata(APIView):
   @method_decorator(cache_page(60))
   @method_decorator(rate_limits(5, 60))
   def get(self,request):
      datas=Data.objects.all()
      serilalized_data=dataserializer(datas,many=True)
      return Response(serilalized_data.data)
      