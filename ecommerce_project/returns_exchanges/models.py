from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=20)
    order_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.order_number

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    product_sku = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product_name

class ReturnExchangeRequest(models.Model):
    RETURN = 'Return'
    EXCHANGE = 'Exchange'
    REQUEST_CHOICES = [
        (RETURN, 'Return'),
        (EXCHANGE, 'Exchange'),
    ]

    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=10, choices=REQUEST_CHOICES)
    reason = models.TextField()
    status = models.CharField(max_length=20, default='Pending')
    request_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.request_type} - {self.order_item.product_name}"
