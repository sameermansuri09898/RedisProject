from django.urls import path
from .views import studentview,studentget,Fetchdata
from rest_framework import routers

urlpatterns=[
  path('student-list/',studentview.as_view()),
  path('studentlist/',studentget.as_view()),
  path('buggdata/',Fetchdata.as_view()),
]