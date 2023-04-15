from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a product name')
    brand = models.CharField(max_length=100, default=' ')
    price = models.IntegerField()

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Cart {self.id} for {self.user.username}'

    def cart_items(self):
        return CartItem.objects.filter(cart=self)

    @property
    def total_price(self):
        return sum(item.total_price for item in self.cart_items())


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} x {self.product.name} (Price: ${self.product.price}) in cart {self.cart.id}'

    @property
    def total_price(self):
        return self.quantity * self.product.price







