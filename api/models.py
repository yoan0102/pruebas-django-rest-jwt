
from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = CloudinaryField('image', default='')
    category = models.ForeignKey(
        Category, related_name='Products', on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=11, blank=True, null=True)
    address = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    code = models.CharField(max_length=10)
    date_order = models.DateField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.RESTRICT)


class OrderProduct(models.Model):
    order = models.ForeignKey(
        Order, related_name='order_product', on_delete=models.RESTRICT)
    product = models.ForeignKey(
        Product, on_delete=models.RESTRICT)
    quantity = models.IntegerField(default=1)
