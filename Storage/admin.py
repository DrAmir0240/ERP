from django.contrib import admin

from Storage.models import Category, Cargo, CargoImage


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'vulnerability', 'description')
    search_fields = ('name', 'vulnerability')


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo_id', 'name', 'category', 'owner', 'manager', 'weight', 'value', 'date_added')
    search_fields = ('cargo_id', 'name')
    list_filter = ('category', 'manager', 'date_added')
    readonly_fields = ('cargo_id', 'slug', 'date_added')

@admin.register(CargoImage)
class CargoImageAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'image', 'uploaded_at')
