from django.contrib import admin
from .models import Cart, Booking, Coupon

#Cart
@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'car', 'rent_days', 'order_price']


# Bookimg
@admin.register(Booking)
class BookingModelAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'car','rent_days','user_pay','remaning_amount','status']

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'discount_percentage', 'valid_from', 'valid_to', 'active']

