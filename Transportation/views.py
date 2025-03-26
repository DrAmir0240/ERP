from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from Storage.models import Category
from Storage.serializers import CategorySerializer
from Users.models import Driver, Manager
from Users.serializers import DriverSerializer, ManagerSerializer
from .models import TransportCar
from .serializers import TransportCarSerializer


# Create your views here.
class TransportCarCreateAPIView(generics.CreateAPIView):
    queryset = TransportCar.objects.all()
    serializer_class = TransportCarSerializer


    def get(self, request, *args, **kwargs):
        drivers = Driver.objects.all()
        managers = Manager.objects.all()
        categories = Category.objects.all()

        driver_serializer = DriverSerializer(drivers, many=True)
        manager_serializer = ManagerSerializer(managers, many=True)
        category_serializer = CategorySerializer(categories, many=True)

        return Response({
            "drivers": driver_serializer.data,
            "managers": manager_serializer.data,
            "categories": category_serializer.data,
        }, status=status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):
        data = request.data

        driver_id = data.get("driver")
        manager_id = data.get("manager")
        transport_type_id = data.get("transport_type")

        errors = {}

        if not Driver.objects.filter(id=driver_id).exists():
            errors["driver"] = [f"Driver with id {driver_id} does not exist."]

        if not Manager.objects.filter(id=manager_id).exists():
            errors["manager"] = [f"Manager with id {manager_id} does not exist."]

        if not Category.objects.filter(id=transport_type_id).exists():
            errors["transport_type"] = [f"Transport Type with id {transport_type_id} does not exist."]

        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)


class TransportCarListAPIView(generics.ListAPIView):
    queryset = TransportCar.objects.all().order_by('license_plate')
    serializer_class = TransportCarSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_summary="لیست ماشین‌های حمل‌ونقل (مرتب‌شده بر اساس شماره پلاک)",
        responses={200: TransportCarSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

