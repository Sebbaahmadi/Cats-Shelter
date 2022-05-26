import email
from unicodedata import name
from django.db import models

# Create your models here. (Create the field that will be in our contact page)
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=200)
    message=models.TextField()
    
    #to rename the 
    def __str__(self) :
        return self.name

