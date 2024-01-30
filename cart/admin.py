from django.contrib import admin
from .models import Cart, Booking

#Cart
@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'car', 'rent_days', 'order_price']


# Bookimg
@admin.register(Booking)
class BookingModelAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'car','rent_days','order_date','status']

