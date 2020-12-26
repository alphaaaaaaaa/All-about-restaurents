from django.db import models

# Create your models here.

class Dish(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='img/dishes/')
    image_url = models.CharField(max_length=150,default='sd') 
    description = models.TextField()
    rating = models.CharField(max_length=5)
    category = models.CharField(max_length=30)
    price = models.IntegerField(default=10)

class Restaurent(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='img/restaurents/')
    image_url = models.CharField(max_length=150,default='sd') 
    category = models.CharField(max_length=30,default=None)
    description = models.TextField(default=None)
    rating = models.CharField(max_length=5)
    address = models.CharField(max_length=200,default=None)
    Dishes = models.ManyToManyField(Dish,default=None)


