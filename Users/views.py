from rest_framework import generics, status
from rest_framework.generics import RetrieveAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.authtoken.models import Token
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate

from .models import Driver, Customer, Manager, MainManager
from .serializers import DriverSerializer, CustomerSerializer, ManagerSerializer, DriverListSerializer, \
    ManagerListSerializer, CustomerListSerializer, ManagerProfileSerializer, MainManagerProfileSerializer, \
    DriverProfileSerializer, MainManagerSerializer




# 📌 پروفایل‌ها
class MainManagerProfileView(generics.RetrieveAPIView):
    queryset = MainManager.objects.all()
    serializer_class = MainManagerProfileSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ManagerProfileView(generics.RetrieveAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerProfileSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class DriverProfileView(generics.RetrieveAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverProfileSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


# 📌 ایجاد کاربران
class MainManagerCreateAPIView(generics.CreateAPIView):
    queryset = MainManager.objects.all()
    serializer_class = MainManagerSerializer
    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ManagerCreateAPIView(generics.CreateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class DriverCreateAPIView(generics.CreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CustomerCreateAPIView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


# 📌 لیست‌ها
class DriverListAPIView(generics.ListAPIView):
    queryset = Driver.objects.all().order_by('-rate')
    serializer_class = DriverListSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ManagerListAPIView(generics.ListAPIView):
    queryset = Manager.objects.all().order_by('-balance')
    serializer_class = ManagerListSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CustomerListAPIView(generics.ListAPIView):
    queryset = Customer.objects.all().order_by('-date_joined')
    serializer_class = CustomerListSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
