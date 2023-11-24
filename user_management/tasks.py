from celery import shared_task
from utils.sms import send_sms
from .models import Manager
from product.models import Product


@shared_task
def send_restock_sms():
    restock_products = Product.objects.needs_restock()
    for manager in Manager.objects.all():
        for product in restock_products:
            message = f"Product {product.name} needs restocking. Current stock: {product.stock}"
            send_sms(manager.phone, message)
