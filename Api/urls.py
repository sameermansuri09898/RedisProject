from django.urls import path
from .views import studentview,studentget
from rest_framework import routers

urlpatterns=[
  path('student-list/',studentview.as_view()),
  path('studentlist/',studentget.as_view()),
]