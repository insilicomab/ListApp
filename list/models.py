from django.db import models

class ListModel(models.Model):
   item = models.CharField(max_length=100) 

   def __str__(self):
       return self.item