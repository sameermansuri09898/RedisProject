from django.db import models

class student(models.Model):
  name=models.CharField()
  section=models.CharField()
  Clas=models.CharField()


  def __str__(self):
    return super().__str__()