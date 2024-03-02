from http.client import ACCEPTED
from django.db import models
from numpy import product
from account.models import User
from products.models import Product

# Cart.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Product, on_delete=models.CASCADE)
    pickup_date = models.DateField(null=True)
    pickup_time = models.CharField(max_length=100, default="None", null=True)
    dropoff_date = models.DateField(null=True)
    dropoff_time = models.CharField(max_length=100, default="None", null=True)
    pickup_point = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=100, default="None", null=True)
    seller_car_location = models.CharField(max_length=255, null=True)
    rent_days = models.PositiveIntegerField(default=1)
    user_name = models.CharField(max_length=100, default="None", null=True)
    user_phone = models.IntegerField(default = 123456789, null=True)
    user_address = models.CharField(max_length=200, default="None", null=True)
    insurance_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    custom_deposit = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    order_price = models.FloatField(default=0 , null=True)
    remaning_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    cart_date = models.DateTimeField(auto_now_add=True, null=True)

BOOKING_STATUS = (
    ('Pending','Pending'),
    ('Booked','Booked'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('DropOff','DropOff'),
    ('Late','Late'),
    ('Cancel','Cancel'),

)


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Product, on_delete=models.CASCADE)
    pickup_date = models.DateField()
    pickup_time = models.CharField(max_length=100, default="None", null=True)
    dropoff_date = models.DateField(null=True)
    dropoff_time = models.CharField(max_length=100, default="None", null=True)
    pickup_point = models.CharField(max_length=255)
    city = models.CharField(max_length=100, default="None", null=True)
    seller_car_location = models.CharField(max_length=255)
    rent_days = models.PositiveIntegerField(default=1)
    user_name = models.CharField(max_length=100, default="None", null=True)
    user_phone = models.IntegerField(default = 123456789, null=True)
    user_address = models.CharField(max_length=200, default="None", null=True)
    insurance_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    custom_deposit = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    user_pay = models.FloatField(default=0 , null=True)
    remaning_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=150, choices=BOOKING_STATUS, default="Pending")