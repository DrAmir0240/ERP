from rest_framework import serializers

from Financial.serializers import OrderSerializer, PaymentSerializer
from Storage.serializers import CargoSerializer
from Users.models import Manager
from Users.serializers import DriverSerializer, CustomerSerializer
from .models import TransportCar

class TransportCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportCar
        fields = '__all__'


class OrganizationProfileSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(source='order_set', many=True)
    payments = PaymentSerializer(source='payment_set', many=True)
    drivers = DriverSerializer(source='drivers', many=True)
    customers = CustomerSerializer(source='customer_set', many=True)
    cargos = CargoSerializer(source='cargo_set', many=True)
    total_orders = serializers.SerializerMethodField()

    class Meta:
        model = Manager
        fields = ['id', 'full_name', 'balance', 'orders', 'payments', 'drivers', 'customers', 'cargos', 'total_orders']

    def get_total_orders(self, obj):
        return obj.order_set.count()






