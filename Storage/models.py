from django.db import models
from autoslug import AutoSlugField
from Users.models import Customer, Manager


# Create your models here.
class Category(models.Model):
    VULNERABILITY_CHOICES = [
        ('very_vulnerable', 'Very Vulnerable'),
        ('high', 'High'),
        ('medium', 'Medium'),
        ('no_need_to_worry', 'No Need to Worry'),
    ]
    name = models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True)
    picture = models.ImageField(upload_to='category_pictures')
    vulnerability = models.CharField(max_length=100, choices=VULNERABILITY_CHOICES)
    description = models.TextField()

    def __str__(self):
        return self.name


class Cargo(models.Model):
    cargo_id = models.CharField(max_length=100, unique=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    owner = models.ForeignKey(Customer, on_delete=models.PROTECT)
    manager = models.ForeignKey(Manager, on_delete=models.PROTECT)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    date_added = models.DateField(auto_now_add=True)

    def generate_cargo_id(self):
        return f'{self.date_added}-{self.owner.id}-{self.manager.id}-{self.category.id}'

    def __str__(self):
        return self.cargo_id


class CargoImage(models.Model):
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='cargo_images')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.cargo.name}"