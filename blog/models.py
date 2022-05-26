from cgitb import text
from django.db import models

# Create your models here.
#interint all my models 
#to save it a table in a DB
class blog(models.Model):
    titel=models.CharField(max_length=100)
    text=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.titel

 # Tehen go to admin to rigister      


