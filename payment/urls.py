from django.urls import path

from payment import views

urlpatterns = [
    path('item/<int:pk>', views.get_item, name='item'),
]
