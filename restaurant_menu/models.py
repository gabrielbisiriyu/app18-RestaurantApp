from django.db import models  
from django.contrib.auth.models import User # NOTE User IS A TABLE JUST LIKE ITEM
MEAL_TYPE = (('starters','Starters'),('salads','Salads'),
('main_dishes','Main Dishes'),('deserts','Deserts')) 

STATUS = ((0,"Unavailable"),(1,"Available"))

class Item(models.Model):
    meal = models.CharField(max_length=1000,unique=True) # unique=True PREVENTS HAVING DUPLIUCATE MEALS 
    description = models.CharField(max_length=2000)  
    price = models.DecimalField(max_digits=10,decimal_places=2) 
    meal_type = models.CharField(max_length=200,choices = MEAL_TYPE) # WE USE choices WHEN WE HAVE A FINITE NUMBER OF DATA
    author = models.ForeignKey(User,on_delete=models.PROTECT) 
    status = models.IntegerField(choices=STATUS,default=0)
    date_created = models.DateField(auto_now_add=True) 
    date_updated = models.DateField(auto_now=True) 

    def __str__(self):
        return self.meal     



        