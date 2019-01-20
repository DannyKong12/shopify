from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    inventory = models.IntegerField()
    company = models.ForeignKey(Company, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Cart(models.Model):
    userId = models.CharField(max_length=100, default="")
    items = models.ManyToManyField(CartItem)
