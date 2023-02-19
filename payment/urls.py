from django.urls import path

from payment import views

urlpatterns = [
    path('item/<int:pk>', views.item, name='item'),
    path('buy/success', views.success, name='success'),
    path('buy/cancel', views.cancel, name='cancel'),
    path('buy/<int:pk>', views.buy, name='buy'),
]
