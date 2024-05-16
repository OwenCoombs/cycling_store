from django.db import models

# Create your models here.

class Vehicle(models.Model):
    VEHICLE_TYPES = [
        ('unicycle', 'Unicycle'),
        ('bicycle', 'Bicycle'),
        ('tricycle', 'Tricycle'),
    ]
    type = models.CharField(max_length=20, choices=VEHICLE_TYPES)
    number_in_stock = models.PositiveIntegerField()

class Customer(models.Model):
    name = models.CharField(max_length=100)

class CustomerOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ManyToManyField(Vehicle)
    created_date = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
