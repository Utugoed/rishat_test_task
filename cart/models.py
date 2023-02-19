from functools import reduce

from django.db import models

from payment import models as payment_models


class Order(models.Model):
    @property
    def total_price(self):
        items = self.items.all()
        if len(items) == 1:
            return items[0].total_price
        return reduce(lambda a, b: a.total_price + b.total_price, items)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(payment_models.Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, validators=[payment_models.validate_positive])

    @property
    def total_price(self):
        return self.product.price * self.quantity

