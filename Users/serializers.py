from rest_framework import serializers

from Financial.models import Order
from .models import Manager, Driver, Customer, MainManager


class MainManagerProfileSerializer(serializers.ModelSerializer):
    all_managers = serializers.SerializerMethodField()

    class Meta:
        model = MainManager
        fields = ["full_name", "access_code", "picture", "grand_balance", "all_managers"]

    def get_all_managers(self, obj):
        managers = Manager.objects.all()
        return [
            {
                "manager_id": manager.id,
                "name": manager.full_name,
                "total_orders": manager.order_set.count(),

            }
            for manager in managers
        ]


class ManagerProfileSerializer(serializers.ModelSerializer):
    managed_cargos = serializers.SerializerMethodField()
    managed_orders = serializers.SerializerMethodField()
    managed_drivers = serializers.SerializerMethodField()
    managed_customers = serializers.SerializerMethodField()
    managed_payments = serializers.SerializerMethodField()
    managed_cars = serializers.SerializerMethodField()

    class Meta:
        model = Manager
        fields = [
            "full_name", "employee_id", "picture", "balance",
            "managed_cargos", "managed_orders", "managed_drivers",
            "managed_customers", "managed_payments", "managed_cars"
        ]

    def get_managed_cargos(self, obj):
        return [{"cargo_id": cargo.id, "name": cargo.name} for cargo in obj.cargo_set.all()]

    def get_managed_orders(self, obj):
        return [{"order_id": order.id, "cargo": order.cargo.name} for order in obj.order_set.all()]

    def get_managed_drivers(self, obj):
        return [{"driver_id": driver.id, "name": driver.full_name} for driver in obj.drivers.all()]

    def get_managed_customers(self, obj):
        orders = obj.order_set.all()
        customers = set(order.cargo.owner for order in orders)
        return [{"customer_id": customer.id, "name": customer.full_name} for customer in customers]

    def get_managed_payments(self, obj):
        orders = obj.order_set.all()
        payments = [payment for order in orders for payment in order.payment_set.all()]
        return [{"payment_id": payment.id, "amount": payment.amount} for payment in payments]

    def get_managed_cars(self, obj):
        return [{"car_id": car.id, "license_plate": car.license_plate} for car in obj.transportcar_set.all()]


class DriverProfileSerializer(serializers.ModelSerializer):
    orders = serializers.SerializerMethodField()

    class Meta:
        model = Driver
        fields = ["full_name", "drive_license_id", "picture", "debt_balance", "travel_count", "rate", "orders"]

    def get_orders(self, obj):
        orders = Order.objects.filter(driver=obj)
        return [{"order_id": order.id, "cargo": order.cargo.name, "car": order.car.license_plate} for order in orders]


class MainManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainManager
        fields = ['id', 'full_name', 'email', 'password', 'access_code', 'picture', 'grand_balance']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = MainManager(**validated_data)
        if password:
            instance.set_password(password)  # هش کردن رمز عبور
        instance.save()
        return instance


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['email', 'full_name', 'password', 'employee_id', 'picture', 'balance', 'management_date']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        manager = Manager.objects.create_user(
            email=validated_data['email'],
            full_name=validated_data['full_name'],
            password=validated_data['password'],
            employee_id=validated_data['employee_id'],
            picture=validated_data.get('picture', None),
            balance=validated_data.get('balance', 0),
        )
        return manager


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['email', 'full_name', 'password', 'drive_license_id', 'assigned_manager', 'picture', 'debt_balance',
                  'travel_count', 'rate']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        driver = Driver.objects.create_user(
            email=validated_data['email'],
            full_name=validated_data['full_name'],
            password=validated_data['password'],
            drive_license_id=validated_data['drive_license_id'],
            assigned_manager=validated_data['assigned_manager'],
            picture=validated_data.get('picture', None),
            debt_balance=validated_data.get('debt_balance', 0),
            travel_count=validated_data.get('travel_count', 0),
            rate=validated_data.get('rate', 0),
        )
        return driver


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['email', 'full_name', 'password', 'social_security_number', 'picture', 'business_field',
                  'wallet_balance']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        customer = Customer.objects.create_user(
            email=validated_data['email'],
            full_name=validated_data['full_name'],
            password=validated_data['password'],
            social_security_number=validated_data['social_security_number'],
            picture=validated_data.get('picture', None),
            business_field=validated_data.get('business_field', ''),
            wallet_balance=validated_data.get('wallet_balance', 0),
        )
        return customer


class ManagerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['id', 'email', 'full_name', 'employee_id', 'picture', 'balance', 'management_date']


class DriverListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['id', 'email', 'full_name', 'drive_license_id', 'assigned_manager', 'picture', 'debt_balance',
                  'travel_count', 'rate']


class CustomerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'email', 'full_name', 'social_security_number', 'picture', 'business_field', 'wallet_balance',
                  'date_joined']
