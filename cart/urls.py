from django.urls import path

from cart import views

urlpatterns = [
    path('orders/<int:pk>', views.get_order, name='order'),
    path('orders/make_from_product/<int:pk>', views.make_from_product, name='make_from_product'),
    path('buy/success', views.success, name='success'),
    path('buy/cancel', views.cancel, name='cancel'),
    path('buy/<int:pk>', views.buy, name='buy')
]