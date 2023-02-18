from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Brand = models.CharField(max_length=50, null=False)
    year = models.CharField(max_length=4,null=True)
    price = models.CharField(max_length=15,null=False)
    description = models.TextField(max_length = 2000,null =True, blank=True)
    city = models.CharField(max_length=50,null = False)
    contact_number = models.CharField(max_length=11,null=False) 
    picture = models.ImageField(null = True, blank=True)
    favourite = models.ManyToManyField(User,related_name='favouriteCar', blank =True)
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-updated','-created']
     
    def __str__(self):
        return self.Brand

class Services(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False)
    description = models.TextField(max_length = 2000,null =True, blank=True)
    city = models.CharField(max_length=50,null = False)
    contact_number = models.CharField(max_length=11,null=False) 
    favourite = models.ManyToManyField(User,related_name='favouriteService', blank =True)
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.title


class Auto_parts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=11,null=False) 
    part_name = models.CharField(max_length=50, null=False)
    city = models.CharField(max_length=50,null = False)
    cost = models.CharField(max_length=15, null=False)
    for_car = models.CharField(max_length = 50,null =True, blank=True)
    favourite = models.ManyToManyField(User,related_name='favouriteAutoPart', blank =True)
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.part_name

