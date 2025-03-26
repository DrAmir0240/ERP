from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Order, Payment, Cargo, Driver, TransportCar, Manager
from .serializers import OrderSerializer, PaymentSerializer
from Storage.serializers import CargoSerializer
from Users.serializers import DriverSerializer, ManagerSerializer
from Transportation.serializers import TransportCarSerializer


# Create your views here.
class OrderCreateAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


    def get(self, request, *args, **kwargs):
        """ لیست مدیران، رانندگان، خودروها و محموله‌ها را برمی‌گرداند """
        managers = Manager.objects.all()
        drivers = Driver.objects.all()
        cars = TransportCar.objects.all()
        cargos = Cargo.objects.all()

        return Response({
            "managers": ManagerSerializer(managers, many=True).data,
            "drivers": DriverSerializer(drivers, many=True).data,
            "cars": TransportCarSerializer(cars, many=True).data,
            "cargos": CargoSerializer(cargos, many=True).data
        }, status=status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):
        """ایجاد سفارش جدید"""
        return super().post(request, *args, **kwargs)


class PaymentCreateAPIView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


    def get(self, request, *args, **kwargs):
        """ لیست سفارشات را برمی‌گرداند تا در فرم پرداخت استفاده شود """
        orders = Order.objects.all()

        return Response({
            "orders": OrderSerializer(orders, many=True).data
        }, status=status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):
        """ایجاد پرداخت جدید"""
        return super().post(request, *args, **kwargs)
