# from django.db import models
# from django.conf import settings
# from myapp.models import Product


# class Order(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Order {self.id} by {self.user}"


# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.PROTECT)
#     quantity = models.PositiveIntegerField()
#     price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2)

#     @property
#     def subtotal(self):
#         return self.price_at_purchase * self.quantity

#     def __str__(self):
#         return f"{self.quantity} x {self.product} (Order {self.order.id})"
