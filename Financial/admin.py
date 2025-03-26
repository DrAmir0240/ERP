from django.contrib import admin

from Financial.models import Order, Payment


# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'driver', 'car', 'manager', 'send_date', 'delivery_date', 'storage_period', 'transport_distance', 'transport_range')
    search_fields = ('cargo__name', 'driver__full_name', 'manager__full_name')
    list_filter = ('transport_range', 'send_date', 'delivery_date')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'amount', 'payment_method')
    search_fields = ('order__cargo__name',)
    list_filter = ('payment_method',)