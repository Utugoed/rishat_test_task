from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import redirect, render
import stripe

from payment.models import Item
from payment.stripe import stripe
from rishat.settings import APP_HOST, APP_PORT, STRIPE_PUBLIC_KEY

def item(request, pk: int):
    item = Item.objects.all().filter(pk=pk)
    if not item:
        return HttpResponseNotFound("Item was not found")
    return render(
        request,
        template_name="payment/item.html",
        context={"item": item[0], "checkout_public_key": STRIPE_PUBLIC_KEY}
    )


def success(request):
    return HttpResponse(content='Buy was successful')


def cancel(request):
    return HttpResponse(content='Buy was canceled')


def buy(request, pk: int):
    item = Item.objects.get(pk=pk)
    if not item:
        return HttpResponseNotFound("Item was not found")
    
    session = stripe.checkout.Session.create(
        line_items=[{
            'price': item.stripe_price_id,
            'quantity': 1,
        }],
        mode='payment',
        success_url=f'http://{APP_HOST}:{APP_PORT}/buy/success',
        cancel_url=f'http://{APP_HOST}:{APP_PORT}/buy/cancel',
    )

    return JsonResponse(data={"session_id": session.id})
