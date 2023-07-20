from django.db import models

# Create your models here.
class Customers(models.Model):
    
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    itempurchase=models.TextField(null=True)
    prices=models.TextField(null=True)
    quantities=models.TextField(null=True)
    def __str__(self):
        return self.name


# class Order(models.Model):
#     itempurchase=models.TextField()
#     prices=models.TextField()
#     quantities=models.TextField()
#     customer= models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)

#     def __str__(self):
#         return self.name




