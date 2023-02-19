from django.contrib import admin

from payment.models import Item
from payment.stripe import stripe

# Register your models here.
class AdminItem(admin.ModelAdmin):
    fields = ['name', 'description', 'price']
    def save_model(self, request, obj, form, change):
        
        item_product = stripe.Product.create(
            name=obj.name,
            description=obj.description,
        )

        item_price = stripe.Price.create(
            unit_amount=int(obj.price * 100),
            currency="rub",
            product=item_product['id'],
        )

        obj.stripe_price_id = item_price["id"]
        obj.save()


admin.site.register(Item, AdminItem)