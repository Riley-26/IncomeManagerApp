from typing import Any
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.name
    

class Income(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, unique=False)
    amount = models.IntegerField()
    
    def __str__(self):
        return self.name
    

class Expense(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, unique=False)
    amount = models.IntegerField()
    
    def __str__(self):
        return self.name
    