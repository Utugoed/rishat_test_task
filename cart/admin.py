from django.contrib import admin

from cart.models import Order, OrderItem


class OrederItemInline(admin.StackedInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrederItemInline
    ]

admin.site.register(Order, OrderAdmin)
