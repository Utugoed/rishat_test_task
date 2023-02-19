from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render

from cart.models import Order, OrderItem
from payment.models import Item
from payment.stripe import stripe
from rishat.settings import APP_HOST, APP_PORT, STRIPE_PUBLIC_KEY


def get_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(
        request,
        template_name="cart/order.html",
        context={"order": order, "checkout_public_key": STRIPE_PUBLIC_KEY}
    )

def make_from_product(request, pk):
    order = Order()
    order.save()

    order_item = OrderItem(
        order=order,
        product=get_object_or_404(Item, pk=pk),
        quantity=1
    )
    order_item.save()

    order.items.set([order_item])
    order.save()
    return JsonResponse(data={"order_id": order.pk})

def success(request):
    return HttpResponse(content='Buy was successful')


def cancel(request):
    return HttpResponse(content='Buy was canceled')

def buy(request, pk: int):
    order = get_object_or_404(Order, pk=pk)

    session = stripe.checkout.Session.create(
        line_items=[{
            'price': item.product.stripe_price_id,
            'quantity': item.quantity,
        } for item in order.items.all()],
        mode='payment',
        success_url=f'http://{APP_HOST}:{APP_PORT}/buy/success',
        cancel_url=f'http://{APP_HOST}:{APP_PORT}/buy/cancel',
    )

    return JsonResponse(data={"session_id": session.id})