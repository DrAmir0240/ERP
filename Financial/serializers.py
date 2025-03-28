from rest_framework import serializers
from .models import Order, Payment, Cargo, Driver, TransportCar, Manager

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'