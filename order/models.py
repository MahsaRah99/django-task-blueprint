from django.db import models
from order.enums import OrderStatus
from order.querysets import OrderQuerySet
from product.models import Product


class Order(models.Model):
    customer = models.ForeignKey("user_management.Customer", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20, default=OrderStatus.PENDING, choices=OrderStatus.choices
    )
    total_price = models.FloatField(default=0)

    objects = OrderQuerySet.as_manager()

    def calculate_total_price(self, product=None):
        total_price = sum(
            item.product.price * item.quantity for item in self.items.all()
        )
        if product:
            total_price += product.price
        return round(total_price, 2)

    def pending(self):
        self.status = OrderStatus.PENDING
        self.save()

    def accept(self):
        self.status = OrderStatus.ACCEPTED
        self.save()

    def reject(self):
        self.status = OrderStatus.REJECTED
        self.save()

    def deliver(self):
        self.status = OrderStatus.DELIVERED
        self.save()

    def cancel(self):
        self.status = OrderStatus.CANCELLED
        self.save()


class OrderItem(models.Model):
    order = models.ForeignKey(
        "order.Order", on_delete=models.CASCADE, related_name="items"
    )
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.order.customer.user.username} - {self.product.name}"

    # def create(self, *args, **kwargs):
    #     print(self.product.id)
    #     super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        """You can not modify this method"""
        self.order.total_price = self.order.calculate_total_price()
        self.order.save()
        super().save(*args, **kwargs)
