from django.db import models

class student(models.Model):
  name=models.CharField()
  section=models.CharField()
  Clas=models.CharField()





  def __str__(self):
    return super().__str__()
  
class Data(models.Model):
    client_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.client_name
  