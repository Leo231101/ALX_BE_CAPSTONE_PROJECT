from django.conf import settings
from django.db import models
from products.models import Product

class Order(models.Model):
    Order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order {self.order_id} by {self.user.username} for {self.product.name}'
