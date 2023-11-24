from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from order.models import OrderItem

# @receiver(post_save, sender=OrderItem)
# def update_total_price(sender, instance, **kwargs):
#         instance.order.total_price += instance.product.price

@receiver(pre_save, sender=OrderItem)
def update_order_on_orderitem_save(sender, instance, **kwargs):
    # If a new OrderItem is created
        order = instance.order
        product = instance.product
        order.calculate_total_price(product)
        # print(product)
