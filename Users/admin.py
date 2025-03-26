from django.contrib import admin

from Users.models import MainManager, Manager, Driver, Customer


# Register your models here.


@admin.register(MainManager)
class MainManagerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'access_code', 'grand_balance')
    search_fields = ('access_code', 'full_name')
    ordering = ('full_name',)


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'employee_id', 'balance', 'management_date')
    search_fields = ('employee_id', 'full_name')
    ordering = ('full_name',)


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'drive_license_id', 'debt_balance', 'rate')
    search_fields = ('drive_license_id', 'full_name')
    ordering = ('full_name',)



@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'social_security_number', 'wallet_balance')
    search_fields = ('social_security_number', 'full_name')
    ordering = ('full_name',)
