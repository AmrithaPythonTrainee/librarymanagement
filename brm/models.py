from django.db import models

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=50)
    price=models.IntegerField()
    lang=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title