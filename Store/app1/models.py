from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Flower(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField(null=True, blank=True)
    image_url = models.CharField(max_length=2023, blank=True)


    def __str__(self):
        return self.title

class Cart(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        items = models.ManyToManyField(Flower)
        total_price = models.DecimalField(max_digits=10, decimal_places=2)

        def __str__(self):
            return self.total_price

class CartItem(models.Model):
        flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
        cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
        quantity = models.PositiveIntegerField(default=1)

        def __str__(self):
            return f'{self.quantity} x {self.flower}'

        @property
        def total_price(self):
            return self.flower.price * self.quantity
