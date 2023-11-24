from django.db.models import QuerySet, Sum, Count
from django.db.models.functions import Coalesce


class CustomerQuerySet(QuerySet):
    def annotate_with_total_spending(self):
        """returns a queryset of total spending of a customer"""
        return self.annotate(total_spending=Coalesce(Sum("order__total_price"), None))

    def annotate_with_order_count(self):
        """returns a queryset of counting the orders of a customer"""
        return self.annotate(order_count=Count("order"))
