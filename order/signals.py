from django.db.models.signals import post_save
from django.dispatch import receiver
from order.models import OrderItem

# @receiver(pre_save, sender=OrderItem)
# def update_total_price(sender, instance,created, **kwargs):
#    # if created:
#         instance.order.total_price += instance.product.price

# @receiver(post_save, sender=OrderItem)
# def update_order_on_orderitem_save(sender, instance, created, **kwargs):
#     # If a new OrderItem is created
#         order = instance.order
#         product = instance.product
#         order.calculate_total_price(product)
#         print(product)