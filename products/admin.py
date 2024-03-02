from django.contrib import admin
from .models import Category, Brand, Product, Subcategory, Review,CustomDiscount, AvaibleTiming, PickupLocation
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
    list_display = ['id', 'title','brand','category','sub_category','selling_price','discounted_price']
#Rental
@admin.register(CustomDiscount)
class CustomDiscountModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'discount_price','discount_valid_days', 'created_at']