from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Order, OrderItem, ReturnExchangeRequest

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ReturnExchangeRequest)
