from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
import stripe

from payment.models import Item
from rishat.settings import STRIPE_PUBLIC_KEY

def get_item(request, pk: int):
    item = get_object_or_404(Item, pk=pk)
    return render(
        request,
        template_name="payment/item.html",
        context={"item": item, "checkout_public_key": STRIPE_PUBLIC_KEY}
    )
