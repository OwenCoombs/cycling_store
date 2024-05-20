from django.db import models

# Create your models here.

class Vehicle(models.Model):     # Defines the types of vehicles available as choices
    VEHICLE_TYPES = [
        ('unicycle', 'Unicycle'),
        ('bicycle', 'Bicycle'),
        ('tricycle', 'Tricycle'),
    ]
    type = models.CharField(max_length=20, choices=VEHICLE_TYPES) # The type of vehicle, restricted to one of the choices in VEHICLE_TYPES
    number_in_stock = models.PositiveIntegerField() # The number of this type of vehicle currently in stock

class Customer(models.Model):
    name = models.CharField(max_length=100) # The name of the customer, with a maximum length of 100 characters

class CustomerOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE) # if the customer is deleted, the order is also deleted
    order = models.ManyToManyField(Vehicle)  # A many-to-many relationship to the Vehicle model, indicating which vehicles are in the order
    created_date = models.DateTimeField(auto_now_add=True)  # The date and time when the order was created, automatically set when the order is first created
    paid = models.BooleanField(default=False)  # A boolean field to indicate whether the order has been paid for, defaulting to False
