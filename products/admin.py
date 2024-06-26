from django.contrib import admin
from .models import Category, Brand, Product, Subcategory, Review,CustomDiscount, AvaibleTiming, PickupLocation, ProductImages
# Category
admin.site.register(Category)
# SubCategory
admin.site.register(Subcategory)
#brand
admin.site.register(Brand)
#Review
admin.site.register(Review)
#AvaibleTiming
admin.site.register(AvaibleTiming)
admin.site.register(PickupLocation)
PickupLocation
#Product
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','brand','category','sub_category','selling_price','rent_per_day_price']
#Rental
@admin.register(CustomDiscount)
class CustomDiscountModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'discount_price_percentage','seven_day_booking_discount_percentage','valid_from', 'valid_to']

admin.site.register(ProductImages)