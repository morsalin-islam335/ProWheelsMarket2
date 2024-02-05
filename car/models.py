from django.db import models

# Create your models here.
from django.contrib.auth.models import User # ja suer buy korta tar information track rakha hoiba
from company.models import Category
from user.models import Owner
class Car(models.Model):
    name = models.CharField(max_length = 100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField()
    brand = models.ForeignKey(Category, on_delete = models.CASCADE, related_name = 'cars')
    image = models.ImageField(upload_to='car/media/uploads/')
    buyer = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True, related_name = 'cars')
    owner = models.ForeignKey(Owner, on_delete = models.CASCADE ,related_name = 'ownerCars')



    def __str__(self):
        return f"{self.name}"
    

class Comment(models.Model):
    # One to many relationship
    car = models.ForeignKey(Car, on_delete = models.CASCADE, related_name  = 'comments', null = True, blank = True) # we can access title, content etc through related name
    name = models.CharField(max_length = 50)
    body = models.TextField(verbose_name = 'comment')
    comments_time = models.DateTimeField(auto_now_add = True) # jokhon kau ekjon comment korba sei time captue hoiba

    def __str__(self):
        return f'comments by {self.name}'

        