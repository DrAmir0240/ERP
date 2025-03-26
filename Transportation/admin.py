from django.contrib import admin

from Transportation.models import TransportCar


# Register your models here.

@admin.register(TransportCar)
class TransportCarAdmin(admin.ModelAdmin):
    list_display = ('license_plate', 'driver', 'manager', 'brand', 'model', 'type', 'owner', 'transport_type')
    search_fields = ('license_plate', 'brand', 'model')
    list_filter = ('type', 'owner')
