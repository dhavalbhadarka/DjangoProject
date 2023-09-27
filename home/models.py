from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)    
    phone = models.CharField(max_length=120)
    message = models.TextField()
    date = models.DateField()
  
class Apply(models.Model):
    Name = models.CharField(max_length=120)
    Email = models.EmailField(max_length=120)    
    Phone = models.CharField(max_length=120)
    # address = models.CharField(max_length=300)
    # jobRole = models.ChoicesField()
    

    resume = models.FileField(null=False)
    # Message = models.TextField()
    date = models.DateField()