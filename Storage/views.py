from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from Users.models import Driver
from .models import Cargo, CargoImage, Manager, Customer, Category
from .serializers import CargoSerializer, CargoImageSerializer, CategorySerializer
from Users.serializers import DriverSerializer, ManagerSerializer, CustomerSerializer
from django.utils.text import slugify


class CargoCreateAPIView(generics.CreateAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    parser_classes = (MultiPartParser, FormParser)


    def get(self, request, *args, **kwargs):
        """لیست مشتریان، رانندگان، مدیران و دسته‌بندی‌ها برای پر کردن فرم فرانت‌اند"""
        customers = Customer.objects.all()
        drivers = Driver.objects.all()
        managers = Manager.objects.all()
        categories = Category.objects.all()

        return Response({
            "customers": CustomerSerializer(customers, many=True).data,
            "drivers": DriverSerializer(drivers, many=True).data,
            "managers": ManagerSerializer(managers, many=True).data,
            "categories": CategorySerializer(categories, many=True).data,
        }, status=status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):
        """ایجاد محموله جدید به همراه تصاویر"""
        cargo_serializer = CargoSerializer(data=request.data, context={'request': request})
        if cargo_serializer.is_valid():
            cargo = cargo_serializer.save()
            cargo.slug = slugify(f"{cargo.name}-{cargo.cargo_id}")
            cargo.save()

            images = request.FILES.getlist('images')
            for image in images:
                CargoImage.objects.create(cargo=cargo, image=image)

            return Response({"message": "Cargo created successfully!", "cargo": CargoSerializer(cargo).data},
                            status=status.HTTP_201_CREATED)
        return Response(cargo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
