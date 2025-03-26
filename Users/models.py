from django.db import models


# Create your models here.


class MainManager(models.Model):
    full_name = models.CharField(max_length=255)
    access_code = models.CharField(max_length=255, unique=True)
    picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)
    grand_balance = models.DecimalField(max_digits=50, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.full_name} - Access Code: {self.access_code}, Balance: {self.grand_balance}"


class Manager(models.Model):
    full_name = models.CharField(max_length=255)
    employee_id = models.CharField(max_length=255, unique=True)
    picture = models.ImageField(upload_to='manager_pictures', blank=True, null=True)
    balance = models.DecimalField(max_digits=50, decimal_places=2, default=0)
    management_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - Employee ID: {self.employee_id}, Balance: {self.balance}"




class Driver(models.Model):
    full_name = models.CharField(max_length=255)
    drive_license_id = models.CharField(max_length=255, unique=True)
    assigned_manager = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name='drivers')
    picture = models.ImageField(upload_to='driver_pictures', blank=True, null=True)
    debt_balance = models.DecimalField(max_digits=50, decimal_places=2, default=0)
    travel_count = models.IntegerField(default=0)
    rate = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.full_name} - License ID: {self.drive_license_id}, Debt: {self.debt_balance}"


class Customer(models.Model):
    full_name = models.CharField(max_length=255)
    social_security_number = models.CharField(max_length=255, unique=True)
    picture = models.ImageField(upload_to='customer_pictures', blank=True, null=True)
    business_field = models.CharField(max_length=255, blank=True, null=True)
    wallet_balance = models.DecimalField(max_digits=50, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.full_name} - SSN: {self.social_security_number}, Wallet: {self.wallet_balance}"

