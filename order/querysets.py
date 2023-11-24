from django.db.models import QuerySet,Sum


class OrderQuerySet(QuerySet):
    def by_customer(self, customer):
        """Filtering orders by a specific customer"""
        return self.filter(customer=customer)

    def total_price(self):
        """Calculate the total price of all orders in the queryset."""
        return self.aggregate(total_price=Sum('total_price')).get('total_price')

    def total_price_by_customer(self, customer):
        return self

    def submitted_in_date(self, date_value):
        """Filter orders submitted on a specific date."""
        return self.filter(date__date=date_value)