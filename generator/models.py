from django.db import models

# Create your models here.
class Task (models.Model):  #crear el modelo, django crea la tabla
    username = models.CharField(max_length=30)
    password = models.TextField(max_length=30) 
    date = models.TextField(max_length=40)
    
    def __str__(self):
        return  'password created by ' + self.username
